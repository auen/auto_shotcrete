# Automatic shotcrete application

This is the code we developed during our master's Thesis. (Document will be linked when published). It is a framework for automatic operation of the 5-DOF [AMV][amv] 4200H shotcrete applicator. It connects to the onboard microcontroller over CAN bus, reads the sensors, runs the forward kinematics and displays the nozzle pose in a 3D-plot. In addition to monitoring the machine pose it can:

- Create parametric surface model from 5 knot points
- Calculate inverse kinematics


### Installation
The framework has been tested on Python 3.7 (32 and 64 bit) on Windows

  - PyQt5
  - matplotlib
  - numpy
  - python-can
  - scipy

### Running the application
