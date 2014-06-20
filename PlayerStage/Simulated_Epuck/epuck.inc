#Taken from Jenny Owen's Blog
# epuck.inc
# rough model of the epuck robots

#ranger sensors
define epuck_IR ranger
(
	# number of sonars
	scount 8

	# define the pose of each transducer [xpos ypos heading]
	spose[0] [0.030	-0.010	-15]	#fr right
	spose[1] [0.022	-0.025	-45]	#fr right 2
	spose[2] [0.0	-0.031	-90]	# right	
	spose[3] [-0.03   -0.015	-150]	#back right
	spose[4] [-0.03	0.015		150]	#back left
	spose[5] [0.0  	0.031		90]	#left
	spose[6] [0.022	0.025		45]	#fr left 2
	spose[7] [0.03	0.01		15]	#fr left
	
		#angles got from the placement diagram on epuck website.

		
	# define the field of view of each transducer [range_min range_max view_angle]
	sview [0.0064 0.1 10] #[0.0064 0.1 10]
		# range min and max are from the epuck website prox sensor graphs.

	# define the size of each transducer [xsize ysize] in meters
	ssize [0.002 0.002 0.001]
		#from IR data sheet
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
