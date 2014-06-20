#Taken from Jenny Owen's Blog
# epuck.inc
# rough model of the epuck robots
#ranger sensors
define epuck_sonar sensor
(
 size [0.002 0.002 0.001]
 range [0.0064 0.1]
 fov [10]
 samples 1
 color_rgba [0 1 0 0.2]
)

define epuck_IR sonar
(
	# define the pose of each transducer [xpos ypos heading]
	epuck_sonar (pose [0.030	-0.010	0 -15])	#fr right
	epuck_sonar (pose [0.022	-0.025  0 -45])	#fr right 2
	epuck_sonar (pose [0.0	-0.031	0 	-90])	# right	
	epuck_sonar (pose [-0.03   -0.015	0	-150])	#back right
	epuck_sonar (pose [-0.03	0.015	0	150])	#back l
	epuck_sonar (pose [0.0  	0.031	0	90])	#left
	epuck_sonar (pose [0.022	0.025	0	45])	#fr left 2
	epuck_sonar (pose [0.03	0.01	0	15])	#fr left
)

		

# epuck blobfinder
#define epuck_cam ptz
#(
#	blobfinder
#	(
#		# number of colours to look for
#		channels_count 1
#	
#		# which colours to look for
#		channels ["red"]
#	
#		# camera parameters
#		image [640 480]		#resolution
#		range_max 5.00
#		ptz [0 0 0]	
#	)
#	size [0.001 0.001 0.001]
#)

# updates from http://yorkroboticist.blogspot.com/2009/11/update-of-manual-code-from-stage-211-to.html
# kmn 6/3/13

# bigbob's blobfinder
define bigbobs_eyes blobfinder
(
# number of colours to look for
colors_count 2

# which colours to look for
colors ["orange" "DarkBlue"]

# camera parameters
image [160 120]  #resolution
)


# epuck base
define epuck position
(
	# actual size
	size [0.074 0.074 0.053]
	
	# estimated mass in KG
	mass 0.5
	
	#Defining the shape of an epuck
	bitmap "bitmaps/circle.png"
	gui_outline 0
	

	
	# differential steering model
	drive "diff"

	# sensors attached to epuck
	epuck_IR()  
	#epuck_cam()
	obstacle_return 1 # Can hit things.
	laser_return 1 # reflects laser beams
	ranger_return 1 # reflects sonar beams
	#blob_return 1 # Seen by blobfinders
)
