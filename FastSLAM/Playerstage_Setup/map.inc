#Map.inc
#Author: Roland Green


define floorplan model
(
color "gray30" 		#Color Displayed
boundary 1		#Can the robot leave the arena? 

gui_nose 0		#Direction model is facing
gui_grid 0		#Overlayed grid
gui_move 0		#Can the model be dragged and dropped
gui_outline 0		#Outline on the model?
gripper_return 0	#Does the sensor register it?
fiducial_return 0	#Does the sensor register it?
ranger_return 1 	#Does the sensor register it?

obstacle_return 1	#Does the sensor register it?
)

