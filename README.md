# Automatic shotcrete application

This is the code we developed during our master's Thesis. (Document will be linked when published). It is a framework for automatic operation of the 5-DOF [AMV][amv] 4200H shotcrete applicator. It connects to the onboard Danfoss MC024 over CAN bus, reads the sensors, runs the forward kinematics and displays the nozzle pose in a 3D-plot. In addition to monitoring the machine pose it can:

- Create parametric surface model from 5 knot points
- Generate spraying pattern in accordance to selected preferences
- Map pattern to surface
- Calculate inverse kinematics
- Update setpoint for all joints

Consequently, it requires that the microcontroller has closed-loop control of all the joints.


### Installation
The framework has been tested with Python 3.7 (32 and 64 bit) on Windows and requires the following modules:

  - PyQt5
  - matplotlib
  - numpy
  - python-can
  - scipy

In addition, it requires drivers for CAN bus:
  - [Kvaser CANlib drivers][kvaser]


### Running the application
The application uses multiprocessing to circumvent the GIL. This can cause problems when running in a virtual environment. We reccomend running in the system enviromnent. Start the application by running: `python .\main.py`

### Screenshot
![](readme_assets/screenshot.png?raw=true)

### Licence
GNU GPLv3


   [amv]: <http://www.amv.as/en/>
   [kvaser]: <https://www.kvaser.com/download/>
