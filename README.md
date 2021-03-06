# Automatic shotcrete application

This is the code we developed during our [master's Thesis][document]. It is a framework for automatic operation of the 5-DOF [AMV][amv] 4200H shotcrete applicator. It connects to the onboard Danfoss MC024 over CAN bus, reads the sensors, runs the forward kinematics and displays the nozzle pose in a 3D-plot. In addition to monitoring the machine pose it can:

- Create a parametric surface model from 5 knot points
- Generate a spraying pattern in accordance to selected preferences
- Map the pattern to the surface
- Calculate inverse kinematics
- Update setpoints for all joints

Consequently, it requires that the microcontroller has closed-loop control of all the joints.

### Structure
The application is module-based to promote individual development of methods. Physical calculations are split into the following modules:

  - Kinematics
  - Surface transformation
  - Pattern generator

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
The application uses multiprocessing to circumvent the GIL. This can cause problems when running in a virtual environment. We recommend running in the system environment. Start the application by running: `python .\main.py`

### Screenshot
![](readme_assets/screenshot.png?raw=true)

### License
MIT


   [amv]: <https://www.amv-as.no/4200-shotcrete-robot>
   [kvaser]: <https://www.kvaser.com/download/>
   [document]: <http://hdl.handle.net/11250/2622743>
