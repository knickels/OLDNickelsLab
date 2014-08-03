#epuck.inc file for player/stage
#model and sensor data for e-puck
#Author: Roland Green
#Date: 06/05/2014

#Ranger IR Sensors
define epuck_IR_sensor sensor
(	
  #Size of each transducer [x y z] in meters
  size [0.002 0.002 0.001]
  #Range minimum and maximim [min max]
  range [0.0064 0.07]
  #Field of view in degrees 
  fov 10
  #GUI color of ranges
  color_rgba [0 1 0 0.5]
  #Number of samples over fov
  samples 1
)

define epuck_IR ranger
(
epuck_IR_sensor( pose [0.030 -0.010 0 -15] )    #fr right
epuck_IR_sensor( pose [0.022 -0.025 0 -45] )    #fr right 2
epuck_IR_sensor( pose [0.0   -0.031 0 -90] )    # right
epuck_IR_sensor( pose [-0.03 -0.015 0 -150] )   #back right
epuck_IR_sensor( pose [-0.03  0.015 0  150] )   #back left
epuck_IR_sensor( pose [0.0    0.031 0  90] )    #left
epuck_IR_sensor( pose [0.022  0.025 0  45] )    #fr left 2
epuck_IR_sensor( pose [0.03   0.01  0  15] )    #fr left
)

#epuck blobfinder
#define epuck_cam blobfinder
#(
#Number of colors to look for
#colors_count 1
#Which color?
#colors ["red"]
#Camera Parameters
#image [640 480] #resolution
#range 5.00
#outline 0
#)

define epuck position
(
#E-Puck Size
size [0.074 0.074 0.053]
mass 0.5 #Kilograms
	
#E_puck shape
bitmap "bitmaps/circle.png"
gui_outline 0

drive "diff"
localization "odom"
odom_error [0 0.0 0 0.0 0 0.0]
#Attach sensors
epuck_IR()
#epuck_cam()
obstacle_return 1 
#laser_return 1
ranger_return 0
#blob_return 1
)
