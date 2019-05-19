import sys, can, struct, traceback
from time import time, sleep
from math import pi, radians
import numpy as np
from numpy import savetxt
import main_window
import surf_trans as pp
import pattern_generator as pg
import kin
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication, QListWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal, QTimer, QAbstractEventDispatcher, Qt
from multiprocessing import Queue, freeze_support, cpu_count, set_start_method, get_context
from queue import Empty


def generate_pattern(param, point_cloud, cart_queue, dt_queue):

    print("Params", param)
    depth = param[0]
    stroke_spacing_des = param[1]
    vel = param[2]

    d, offset, params = pp.fit(point_cloud)  # (self.point_cloud)

    segments, t_end, stroke_spacing, n = pg.correct_params(d, depth, stroke_spacing_des, vel)
    uv_path = pg.path(depth, stroke_spacing, vel, t_end, n, segments)

    cart_ref = pp.surf(uv_path, params, offset)

    dt = t_end/n
    print("t_end: ", t_end)
    return cart_queue.put(cart_ref), dt_queue.put(dt)


class Main(QMainWindow, main_window.Ui_MainWindow):

    # Static values
    vel_min = 0.05
    vel_max = 0.7
    stroke_spacing_min = 0.1
    stroke_spacing_max = 1.5
    depth_min = 2
    depth_max = 8

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        # Correct this later
        dummy_points = [[8.0, 4.7453950103830715, 1.0],
                        [8.3, 3.966736204580941, 5.5543035725747485],
                        [7.8, 0.9811185945264055, 7.326604185118965],
                        [8.0, -3.6612492782151276, 5.901951891186886],
                        [8.1, -4.7453950103830715, 1.0]]
        # dummy_points.reverse()

        self.knot_points = []
        for i in range(5):
            pos = dummy_points[i]
            self.knot_point_list.addItem(QListWidgetItem(str("X: {:.2f} Y: {:.2f} Z: "
                                                         "{:.2f}".format(pos[0], pos[1], pos[2]))))
            self.knot_points.append(pos)


        # Multiprocessing
        self.cart_ref_out = Queue()
        self.ikin_out = Queue()
        self.mode_flag = Queue()
        self.param_queue = Queue()
        self.point_queue = Queue()
        self.dt_queue = Queue()

        # Plot
        self.plot_widget.canvas.ax.mouse_init()

        # Methods
        self.mythread = MultiprocessThread(self.cart_ref_out, self.ikin_out, self.mode_flag, self.param_queue,
                                           self.point_queue, self.dt_queue)
        self.mythread.cart_done.connect(self.done_cart)
        self.mythread.ik_done.connect(self.done_ik)
        self.mythread.progress.connect(self.update_progressbar)
        self.mythread.start()

        # Update KPI
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_kpi)
        self.timer.start(200)

        # Initialise variables
        self.slider_velocity()
        self.slider_stroke_spacing()
        self.slider_depth()
        self.knot_x = []
        self.knot_y = []
        self.knot_z = []
        self.cart_ref = []
        self.q_ref = []
        self.status = "Idle"
        self.can_status = "Not initialised"
        self.dt = 0

        # Buttons
        self.ik_btn.clicked.connect(self.start_ik)
        self.cart_btn.clicked.connect(self.start_pattern)
        self.toggle_can_btn.clicked.connect(self.toggle_can)
        self.remove_btn.clicked.connect(self.remove_knot_point)
        self.reset_btn.clicked.connect(self.reset_all)
        self.spray_btn.clicked.connect(self.init_spray)

        # Sliders
        self.velocitySlider.sliderMoved.connect(self.slider_velocity)
        self.stroke_spacing_slider.sliderMoved.connect(self.slider_stroke_spacing)
        self.depth_slider.sliderMoved.connect(self.slider_depth)

        # CAN interface
        self.connect_can()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.can_bus.shutdown()
        else:
            event.ignore()

    def toggle_can(self):
        if self.can_status == "Connected":
            self.disconnect_can()
        else:
            self.connect_can()

    def connect_can(self):
        self.can_bus = CANInterface()
        try:
            self.can_bus.start()
            self.can_bus.joy_btn.connect(self.add_knot_point)
            self.can_indicator.setStyleSheet('color: #eff0f1')
            self.can_status = "Connected"
            self.can_bus.progress.connect(self.update_progressbar)
            self.can_bus.spray_error.connect(self.spray_error)
            self.can_bus.spray_done.connect(self.spray_done)
            self.can_bus.can_error.connect(self.can_error)

        except:
            self.can_indicator.setStyleSheet('color: #ff0000')
            self.can_status = "Error"
            QMessageBox.information(self, "Warning", "CAN interface cannot connect")

    def disconnect_can(self):
        self.can_bus.shutdown()
        self.can_indicator.setStyleSheet('color: #eff0f1')
        self.can_status = "Disconnected"

    def plot_path(self):
        self.plot_widget.canvas.ax.clear()
        self.plot_widget.canvas.ax.set_xlabel('X [m]')
        self.plot_widget.canvas.ax.set_ylabel('Y [m]')
        self.plot_widget.canvas.ax.set_zlabel('Z [m]')
        self.plot_widget.canvas.ax.set_aspect('equal')



        # Aspect ratio correction
        max_range = np.array(
            [np.array(self.cart_ref[0]).max() - np.array(self.cart_ref[0]).min(),
             np.array(self.cart_ref[1]).max() - np.array(self.cart_ref[1]).min(),
             np.array(self.cart_ref[2]).max() - np.array(self.cart_ref[2]).min()]).max()

        xb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][0].flatten() + 0.5 * \
            (np.array(self.cart_ref[0]).max() + np.array(self.cart_ref[0]).min())

        yb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][1].flatten() + 0.5 * \
            (np.array(self.cart_ref[1]).max() + np.array(self.cart_ref[1]).min())

        zb = 0.5 * max_range * np.mgrid[-1:2:2, -1:2:2, -1:2:2][2].flatten() + 0.5 * \
            (np.array(self.cart_ref[2]).max() + np.array(self.cart_ref[2]).min())

        for a, b, c in zip(xb, yb, zb):
            self.plot_widget.canvas.ax.plot([a], [b], [c], 'w')

        self.plot_widget.canvas.ax.plot3D(self.cart_ref[0],
                                          self.cart_ref[1],
                                          self.cart_ref[2], c='yellow')
        self.plot_widget.canvas.ax.scatter(self.knot_x, self.knot_y, self.knot_z, c='#DD0000')

        self.plot_widget.canvas.draw()

    def start_pattern(self):
        self.update_progressbar(0)
        # Clear parameter queue
        try:
            while True:
                self.param_queue.get_nowait()
        except Empty:
            pass

        self.param_queue.put([self.depth, self.stroke_spacing_des, self.velocity])

        if len(self.knot_points) >= 5:  # Adjust to maximal number of coefficients in parametric functions
            self.ik_btn.setEnabled(False)
            self.cart_btn.setEnabled(False)
            self.reset_btn.setEnabled(False)
            self.remove_btn.setEnabled(False)
            self.spray_btn.setEnabled(False)

            self.status = "Parametrising surface"
            self.status_indicator.setStyleSheet('color: #ffff00')

            self.q_ref = []
            # Clear output queue
            try:
                while True:
                    self.cart_ref_out.get_nowait()
            except Empty:
                pass

            # Clear flag queue
            try:
                while True:
                    self.mode_flag.get_nowait()
            except Empty:
                pass

            self.point_queue.put(self.knot_points)
            self.param_queue.put([self.depth, self.stroke_spacing_des, self.velocity])
            self.mode_flag.put("Path Gen")
        else:
            QMessageBox.information(self, "Warning", "Collect 5 or more knot points")

    def done_cart(self):
        try:
            self.cart_ref = self.cart_ref_out.get(True)
            self.dt =  self.dt_queue.get(True)
            self.ik_btn.setEnabled(True)
            self.cart_btn.setEnabled(True)
            self.reset_btn.setEnabled(True)
            self.remove_btn.setEnabled(True)
            self.spray_btn.setEnabled(True)
            print("Number of points: ", len(self.cart_ref[1]))
            self.progressBar.setMaximum(len(self.cart_ref[1]))
            print("Cartesian reference stored in variable")
            self.plot_path()
            self.status = "Surface generated"
            self.status_indicator.setStyleSheet('color: #eff0f1')

            savetxt('cart_ref.txt', np.array(self.cart_ref), delimiter='  ')

        except Empty:
            print("No Cartesian reference returned from thread!")

    def start_ik(self):
        if len(self.cart_ref) == 0:
            QMessageBox.information(self, "Warning", "Create spraying plan before calculating inverse kinematics")
        elif len(self.q_ref) > 0:
            QMessageBox.information(self, "Warning", "Inverse kinematics already calculated")
        else:
            self.ik_btn.setEnabled(False)
            self.cart_btn.setEnabled(False)
            self.reset_btn.setEnabled(False)
            self.remove_btn.setEnabled(False)
            self.spray_btn.setEnabled(False)

            self.status = "Calculating inverse kinematics"
            self.status_indicator.setStyleSheet('color: #ffff00')

            # Clear output queue
            try:
                while True:
                    self.ikin_out.get_nowait()
            except Empty:
                pass

            # Clear flag queue
            try:
                while True:
                    self.mode_flag.get_nowait()
            except Empty:
                pass

            self.mode_flag.put("Inverse Kinematics")

    def done_ik(self):
        self.ik_btn.setEnabled(True)
        self.cart_btn.setEnabled(True)
        self.reset_btn.setEnabled(True)
        self.remove_btn.setEnabled(True)
        self.spray_btn.setEnabled(True)

        try:
            self.q_ref = self.ikin_out.get(True, 0.1)

            # print("Shape of ikin", np.shape(np.array(self.q_ref)))

            savetxt('q_ref.txt', np.array(self.q_ref), delimiter='  ')

            print("Joint space reference stored in variable")
            self.status = "Inverse kinematics calculated"
            self.status_indicator.setStyleSheet('color: #eff0f1')

            try:
                kin.lim_check(self.q_ref)
            except Exception as e:
                QMessageBox.information(self, "Error", "{} Reposition vehicle!".format(e))
                self.reset_all()

        except Empty:
            print("No joint space reference returned from thread!")

    def slider_velocity(self):
        self.velocity = self.vel_min + self.velocitySlider.value()/100 * (self.vel_max - self.vel_min)
        self.vel_disp.setText("Velocity: {:.2f} [m/s]".format(self.velocity))

    def slider_stroke_spacing(self):
        self.stroke_spacing_des = self.stroke_spacing_min + self.stroke_spacing_slider.value() / 100 * \
                                  (self.stroke_spacing_max - self.stroke_spacing_min)
        self.stroke_spacing_label.setText("Stroke spacing: {:.2f} [m]".format(self.stroke_spacing_des))

    def slider_depth(self):
        self.depth = self.depth_min + self.depth_slider.value()/100 * (self.depth_max - self.depth_min)
        self.depth_label.setText("Depth: {:.2f} [m]".format(self.depth))

    def add_knot_point(self):
        self.can_bus.joy_btn.disconnect(self.add_knot_point)
        pose = kin.fk(self.can_bus.sensor_values)
        pos = list(pose[:3, 3])
        self.knot_points.append(pos)

        # Plot
        self.plot_widget.canvas.ax.scatter(pos[0], pos[1], pos[2], c='#DD0000')
        self.plot_widget.canvas.draw()
        self.plot_widget.canvas.ax.mouse_init()

        # Add to list in GUI
        self.knot_point_list.addItem(QListWidgetItem(str("X: {:.2f} Y: {:.2f} Z: "
                                                         "{:.2f}".format(pos[0], pos[1], pos[2]))))

        # Cool down
        QTimer.singleShot(1000, self.connect_knot_signal)  # Increase timeout later

    def connect_knot_signal(self):
        self.can_bus.joy_btn.connect(self.add_knot_point)

    def remove_knot_point(self):
        row = self.knot_point_list.currentRow()
        item = self.knot_point_list.item(row)

        if item is not None:
            self.knot_point_list.takeItem(row)
            del self.knot_points[row]

        else:
            QMessageBox.information(self, "Info", "Select which knot point to delete")

    def update_kpi(self):
        pose = kin.fk(self.can_bus.sensor_values)
        pos = list(pose[:3, 3])

        # print("Sensor values: {}".format(self.can_bus.sensor_values))

        self.x_pos.setText("{:.2f} [m]".format(pos[0]))
        self.y_pos.setText("{:.2f} [m]".format(pos[1]))
        self.z_pos.setText("{:.2f} [m]".format(pos[2]))

        self.status_indicator.setText(self.status)
        self.can_indicator.setText(self.can_status)

        if self.knot_points != []:
            self.knot_x, self.knot_y, self.knot_z = zip(*self.knot_points)
        else:
            self.knot_x = []
            self.knot_y = []
            self.knot_z = []

        if len(self.cart_ref) == 0:
            scale = 2
            self.plot_widget.canvas.ax.clear()
            self.plot_widget.canvas.ax.set_xlabel('X [m]')
            self.plot_widget.canvas.ax.set_ylabel('Y [m]')
            self.plot_widget.canvas.ax.set_zlabel('Z [m]')
            self.plot_widget.canvas.ax.set_aspect('equal')
            self.plot_widget.canvas.ax.scatter(self.knot_x, self.knot_y, self.knot_z, c='red')
            self.plot_widget.canvas.ax.set_xlim3d(-5.2, 21.54)
            self.plot_widget.canvas.ax.set_ylim3d(-13.37, 13.37)
            self.plot_widget.canvas.ax.set_zlim3d(-8.81, 17.94)
        else:
            scale = 1
            self.plot_path()

        self.plot_widget.canvas.ax.quiver(pose[0][3], pose[1][3], pose[2][3],
                                         pose[0][2] * scale, pose[1][2] * scale, pose[2][2] * scale,
                                         color=[0.3, 1, 0.2], pivot='tip')
        self.plot_widget.canvas.draw()

    def check_q(self):
        print("Length q:", len(self.mythread.q))

    def update_progressbar(self, value):
        self.progressBar.setValue(value)

    def reset_all(self):
        reply = QMessageBox.question(self, 'Message', "Do you want to reset all parameters?", QMessageBox.Yes
                                     | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.knot_points = []
            self.knot_point_list.clear()
            self.cart_ref = []
            self.q_ref = []
            self.depth_slider.setSliderPosition(50)
            self.stroke_spacing_slider.setSliderPosition(50)
            self.velocitySlider.setSliderPosition(50)
            self.slider_velocity()
            self.slider_stroke_spacing()
            self.slider_depth()
            self.status_indicator.setStyleSheet('color: #eff0f1')
            self.status = "Idle"
            self.update_progressbar(0)
        else:
            pass

    def init_spray(self):
        if len(self.q_ref) == 0:
            QMessageBox.information(self, "Warning", "Calculate inverse kinematics before spraying")
        else:
            reply = QMessageBox.question(self, 'Message', "Move to initial position?", QMessageBox.Yes
                                     | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.ik_btn.setEnabled(False)
                self.cart_btn.setEnabled(False)
                self.reset_btn.setEnabled(False)
                self.toggle_can_btn.setEnabled(False)
                self.remove_btn.setEnabled(False)
                self.spray_btn.setEnabled(False)

                self.can_bus.joy_btn.disconnect(self.add_knot_point)
                self.spray_btn.clicked.disconnect(self.init_spray)
                self.can_bus.counter = 0

                print("q_ref", self.q_ref[0])

                self.can_bus.send_data(self.q_ref[0])
                self.can_bus.joy_btn.connect(self.run_machine)
                self.status = "Waiting for button press"
                self.status_indicator.setStyleSheet('color: #ffff00')
            else:
                pass

    def pause_spray(self):
        self.can_bus.stop_spray()
        self.can_bus.joy_btn.disconnect(self.pause_spray)
        self.can_bus.manual_mode.disconnect(self.pause_spray)

        reply = QMessageBox.question(self, 'Message', "Resume spraying? Remember to enable automatic mode", QMessageBox.Yes
                                     | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.can_bus.timer(self.dt)
            self.can_bus.joy_btn.connect(self.pause_spray)
            self.can_bus.manual_mode.connect(self.pause_spray)
        else:
            self.spray_btn.clicked.disconnect(self.pause_spray)
            self.can_bus.joy_btn.connect(self.add_knot_point)
            self.spray_btn.setText("Spray")
            self.spray_btn.clicked.connect(self.init_spray)
            self.update_progressbar(0)
            self.can_bus.counter = 0
            self.status = "Inverse kinematics calculated"
            self.status_indicator.setStyleSheet('color: #eff0f1')
            self.ik_btn.setEnabled(True)
            self.cart_btn.setEnabled(True)
            self.reset_btn.setEnabled(True)
            self.toggle_can_btn.setEnabled(True)
            self.remove_btn.setEnabled(True)

    def run_machine(self):
        self.can_bus.joy_btn.disconnect(self.run_machine)
        self.spray_btn.clicked.connect(self.pause_spray)
        self.spray_btn.setEnabled(True)
        self.spray_btn.setText("Pause")
        self.status = "Spraying"
        self.can_bus.q_ref = self.q_ref
        self.can_bus.timer(self.dt)
        QTimer.singleShot(1000, self.joy_pause)

    def joy_pause(self):
        self.can_bus.joy_btn.connect(self.pause_spray)
        self.can_bus.manual_mode.connect(self.pause_spray)

    def spray_done(self):
        print("Done spraying!")
        QMessageBox.information(self, "Info", "Done spraying")
        self.status = "Done spraying"
        self.can_bus.joy_btn.disconnect(self.pause_spray)
        self.can_bus.joy_btn.connect(self.add_knot_point)
        self.spray_btn.clicked.disconnect(self.pause_spray)
        self.spray_btn.clicked.connect(self.init_spray)
        self.spray_btn.setText("Spray")
        self.ik_btn.setEnabled(True)
        self.cart_btn.setEnabled(True)
        self.reset_btn.setEnabled(True)
        self.toggle_can_btn.setEnabled(True)
        self.remove_btn.setEnabled(True)
        self.reset_all()

    def spray_error(self):
        self.status = "Spraying aborted"
        self.status_indicator.setStyleSheet('color: #ff0000')
        QMessageBox.information(self, "Warning", "Error in spraying!")
        self.spray_btn.setText("Spray")
        self.can_bus.joy_btn.disconnect(self.pause_spray)
        self.can_bus.joy_btn.connect(self.add_knot_point)
        self.spray_btn.clicked.disconnect(self.pause_spray)
        self.spray_btn.clicked.connect(self.init_spray)
        self.ik_btn.setEnabled(True)
        self.cart_btn.setEnabled(True)
        self.reset_btn.setEnabled(True)
        self.toggle_can_btn.setEnabled(True)
        self.remove_btn.setEnabled(True)

    def can_error(self):
        self.can_indicator.setStyleSheet('color: #ff0000')
        self.can_status = "Error"
        QMessageBox.information(self, "Warning", "Error in CAN bus")


class MultiprocessThread(QThread):

    cart_done = pyqtSignal(bool)
    ik_done = pyqtSignal(bool)
    progress = pyqtSignal(int)

    def __init__(self, cart_ref_out, ikin_out, mode_flag, param_queue, point_q, dt_queue):  # mode_flag
        super(MultiprocessThread, self).__init__()
        self.cartQ = cart_ref_out
        self.ikinQ = ikin_out
        self.flag = mode_flag
        self.param = param_queue
        self.flag.put("Idle Mode")
        self.cart_ref = []
        self.q_ref = []
        self.n = cpu_count()
        self.point_cloud_q = point_q
        self.dt_queue = dt_queue
        freeze_support()
        print("Multiprocess object initialised")

    def run(self):
        while True:
            flag = self.flag.get(block=True)
            print("Multiprocessing mode: {}".format(str(flag)))
            if flag == "Path Gen":
                try:
                    param = self.param.get(block=True)
                except Empty:
                    print("Parameter q empty")
                    break
                point_cloud = self.point_cloud_q.get(block=True)

                self.pattern_process = get_context("spawn").Process(target=generate_pattern, args=(param, point_cloud, self.cartQ, self.dt_queue,))
                self.pattern_process.start()
                try:
                    self.cart_ref = self.cartQ.get(block=True)
                except Empty:
                    print("CartQ is Empty!")
                    break

                self.cartQ.put(self.cart_ref)
                self.flag.put("Idle Mode")
                self.pattern_process.join()
                self.cart_done.emit(True)

            if flag == "Inverse Kinematics":
                if len(self.cart_ref) is 0:
                    print("Provide Cartesian Path")
                    pass
                else:
                    prog = 0
                    with get_context("spawn").Pool(processes=self.n) as self.pool:  # must be guarded with self
                        obj = zip(*self.cart_ref)
                        self.cart_ref.clear()
                        res = self.pool.imap(kin.ik_iter, obj)
                        for i in res:
                            self.q_ref.append(i)
                            prog += 1
                            self.progress.emit(prog)

                        self.ikinQ.put(self.q_ref)
                        sleep(.1)  # need sleep, or queue not ready

                        self.q_ref.clear()
                        self.flag.put("Idle Mode")
                        self.pool.close()
                        self.pool.join()
                        self.ik_done.emit(True)
                        self.progress.emit(0)

            if flag == "stop":
                break


class CANInterface(QThread):
    id_long = 0x183
    id_short = 0x283
    id_button = 0x383
    id_pc = 0x2

    # Offsets and multipliers
    offsets = [-32768, -14364, 57442, -32678, -42962]
    multipliers = [3.46210941710301e-05, 1.94410759575784e-05, 0.000122070312500000, 9.58737992428526e-05,
                   4.79368996214263e-05]

    joy_btn = pyqtSignal(bool)
    progress = pyqtSignal(int)
    spray_error = pyqtSignal(bool)
    spray_done = pyqtSignal(bool)
    can_error = pyqtSignal(bool)
    manual_mode = pyqtSignal(bool)

    def __init__(self):
        QThread.__init__(self)
        self.bus = can.Bus(bustype='kvaser', channel=0, bitrate=1000000)
        print("CAN interface created")

        self.id_f1 = self.id_pc + 0x180
        self.id_f2 = self.id_pc + 0x280

        self.sensor_values = [0, 0, 0, 0, 0]

        self.Btn = False
        self.controller_off = False

        self.update_sensors = False
        self.q_ref = []

        self.counter = 0
        self.dt_timer = QTimer(singleShot=False, timerType=Qt.PreciseTimer)

    def __del__(self):
        self.wait()

    def run(self):
        self.update_sensors = True
        self.start()
        try:
            while self.update_sensors:
                msg = self.bus.recv(0.1)
                # for msg in self.bus:
                if msg.arbitration_id == self.id_short:
                    frame_2 = struct.unpack('!H', msg.data)
                    self.sensor_values[4] = self.multipliers[4] * (frame_2[0] + self.offsets[4])

                if msg.arbitration_id == self.id_long:
                    frame_1 = struct.unpack('!HHHH', msg.data)
                    self.sensor_values[0] = self.multipliers[0] * (frame_1[0] + self.offsets[0])
                    self.sensor_values[1] = self.multipliers[1] * (frame_1[1] + self.offsets[1])
                    self.sensor_values[2] = self.multipliers[2] * (frame_1[2] + self.offsets[2])
                    self.sensor_values[3] = self.multipliers[3] * (frame_1[3] + self.offsets[3])

                if msg.arbitration_id == self.id_button:
                    frame_3 = struct.unpack('!B', msg.data)

                    if frame_3[0] == 1:
                        self.joy_btn.emit(True)
                    elif frame_3[0] == 2:
                        self.manual_mode.emit(True)
                    elif frame_3[0] == 3:
                        self.joy_btn.emit(True)
                        self.manual_mode.emit(True)

        except Exception:
            print("Exception in CAN receive")
            self.can_error.emit(True)

    def shutdown(self):
        self.update_sensors = False
        QTimer.singleShot(1000, self.bus.shutdown)
        print("CAN interface disconnected")

    def timer(self, dt):
        self.dt_timer.timeout.connect(self.msg_send)
        self.dt_timer.start(dt*200)

    def send_data(self, data):

        data_int = []
        for i in range(len(data)):
            num = int(round(data[i] / self.multipliers[i] - self.offsets[i]))

            if num < 0 or num > 2**16:
                raise Exception("Data conversion out of range")
            data_int.append(num)

        data_long = struct.pack('!HHHH', *data_int[0:4])
        data_short = struct.pack('!H', data_int[4])

        msg_long = can.Message(data=data_long, arbitration_id=self.id_f1, is_extended_id=False)
        msg_short = can.Message(data=data_short, arbitration_id=self.id_f2, is_extended_id=False)

        try:
            self.bus.send(msg_long, timeout=0.1)
            self.bus.send(msg_short, timeout=0.1)
            # print("Message sent {}".format(msg_long))
        except can.CanError:
            self.dt_timer.timeout.disconnect(self.msg_send)
            print("x0 message NOT sent at: ", self.counter)
            self.spray_error.emit(True)

    def msg_send(self):
        if self.counter >= len(self.q_ref):
            self.progress.emit(0)
            self.dt_timer.timeout.disconnect(self.msg_send)
            self.spray_done.emit(True)
        else:
            self.send_data(self.q_ref[self.counter])
            self.progress.emit(self.counter)
            self.counter += 1

    def stop_spray(self):
        self.dt_timer.timeout.disconnect(self.msg_send)

def main():
    app = QApplication(sys.argv)
    set_start_method('spawn')
    form = Main()
    # form.showFullScreen()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
