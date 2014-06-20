# Author: Pablo Tarquino (building off of Eric Kang's work)
# This code is similar to playerv.
# It only controls the movement of the robot, it does not connect to the sonars.
# Improvements: Make it so it ONLY moves when key is pressed

import sys
import os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

import math
from playerc import *

#import numpy as np
#from pylab import *

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

# Key Initiation ritual
stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 's' to stop the robot and 'q' to quit.")
stdscr.refresh()

key = ''

# E-puck constants
#   Epuck max speed: 13 cm/s
m_vel = 0.13/2
#   For 13cm/s max speed, max turn in degree/s:
m_spinR = -201.3/4        # Spin clockwise
m_spinL = 201.3/4         # Spin counter clockwise

while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()
    if key == curses.KEY_UP:
        p.set_cmd_vel( 0.8*m_vel, 0.0, 0.0 * math.pi / 180.0, 1) # Move forward
    elif key == curses.KEY_DOWN:
        p.set_cmd_vel( -0.8*m_vel, 0.0, 0.0 * math.pi / 180.0, 1) # Move backward
    elif key == curses.KEY_RIGHT:
        p.set_cmd_vel( 0.0, 0.0, m_spinR * math.pi / 180.0, 1) # Move right
    elif key == curses.KEY_LEFT:
        p.set_cmd_vel( 0.0, 0.0, m_spinL * math.pi / 180.0, 1) # Move left
    elif key == ord('s'):
        p.set_cmd_vel( 0.0, 0.0, 0.0 * math.pi / 180.0, 1) # Stop

curses.endwin()

# Clean up
p.unsubscribe()
c.disconnect()
