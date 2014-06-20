# Author: Pablo Tarquino (building off of Eric Kang's work)
# This code will allow a robot to be controlled using the arrow keys
import sys
import os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

import math
from playerc import *

import curses

# Create a client object
c = playerc_client(None, 'localhost', 6665)
# Connect it
if c.connect() != 0:
  raise playerc_error_str()

# Create a proxy for position2d:0
p = playerc_position2d(c,0)
if p.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise playerc_error_str()

# Retrieve the geometry
if p.get_geom() != 0:
  raise playerc_error_str()
print 'Robot size: (%.3f,%.3f)' % (p.size[0], p.size[1])

# Create a proxy for sonar:0
# (laser is for stage-3, ranger for stage-4)
s = playerc_sonar(c,0)
if s.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise playerc_error_str()

# Retrieve the geometry
if s.get_geom() != 0:
  raise playerc_error_str()
# (pose changed format from stage-3 to stage-4)
#print 'Sonar pose: (%.3f,%.3f,%.3f)' % (s.pose[0],s.pose[1],s.pose[2])
#print 'Laser pose: (%.3f,%.3f,%.3f)' % (s.device_pose.px,s.device_pose.py,s.device_pose.pz)

# Key Initiation ritual
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 's' to stop robot, 'q' to quit")
stdscr.refresh()

key = ''

# E-puck constants
#   Epuck max speed: 13 cm/s
m_vel = 0.13
#   For 13cm/s max speed, max turn in degree/s:
m_spinR = -201.3        # Spin clockwise
m_spinL = 201.3         # Spin counter clockwise

# Define states

s_fwd = 1	# Move forward
s_spinL = 2	# Spin counter clockwise
s_spinR = 3	# Spin clockwise

# Define the initial state

state = s_fwd

# Make function to warn user
def warn():
	if (s.scan[7] < 0.1) | (s.scan[6] < 0.08) | (s.scan[5] < 0.04 | s.scan[0] < 0.1) | (s.scan[1] < 0.08) | (s.scan[2] < 0.04):
		print "Warning! Approaching Wall!"
		print "Hit 's' to stop robot, 'q' to quit"

# Make a function that reads inputs
def read():
	if c.read() == None:
		raise playerc_error_str()

# Need a first read for all others to work
read()

while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    read()
    print p.px
#    warn()
    if key == curses.KEY_UP:
        p.set_cmd_vel( 0.8*m_vel, 0.0, 0.0 * math.pi / 180.0, 1) # Move forward
    elif key == curses.KEY_DOWN:
        p.set_cmd_vel( -0.8*m_vel, 0.0, 0.0 * math.pi / 180.0, 1) # Move backward
    elif key == curses.KEY_RIGHT:
        p.set_cmd_vel( 0.0, 0.0, m_spinR * math.pi / 180.0, 1) # Move backward
    elif key == curses.KEY_LEFT:
        p.set_cmd_vel( 0.0, 0.0, m_spinL * math.pi / 180.0, 1) # Move backward
    elif key == ord('s'):
        p.set_cmd_vel( 0.0, 0.0, 0.0 * math.pi / 180.0, 1) # Stop

curses.endwin()

# Clean up
p.unsubscribe()
s.unsubscribe()
c.disconnect()
