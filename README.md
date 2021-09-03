### Project rolly1 central code repo  

#### Objective  
This repo is used to store all the code used for the rolling home robot. Code meant to run onboard the robot will be placed in a submodule directory.

The code native to this repository is meant to run on the central server computer. 

#### Robot configuration 
**TODO:** Add robot configuration, including kinematics  
The robot consists of a raspberry pi model 3B microcontroller for high-level control, which interfaces through UART with an arduino pro mini for low-level control and sensing. As of now, the gpio pins on the raspberry pi are not used. Communication happens between the pi and the arduino through the pi's usb port, aided by an ftdi converter.  

##### Arduino pinout  
|Pin | Connection | 
|:--:| :---------: |
|3| Left wheel pwm |
|5,6| Left wheel direction|
|9| Right wheel pwm |
|8,7| Right wheel direction|
|10| Left ultrasonic sensor motor control |
|11| Right ultrasonic sensor motor control |
|12| Left ultrasonic sensor trigger |
|13| Left ultrasonic sensor data |
|A0| Right ultrasonic sensor trigger |
|A1| Right ultrasonic sensor data |  

Pin 2 is saved for a  potential future external interrupt 


