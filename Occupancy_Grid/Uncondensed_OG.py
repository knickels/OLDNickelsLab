# Author: Pablo Tarquino (building off of Eric Kang's work)
# First "real-time" mapping program.
# Notes: It needs external program to operate robot (playerv, etc.)
#      Improvement: Make faster response time
#      Improvement: Make continuous plotting, not just when it changes direction
# This version uses large blocks

import sys
import os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

import math
from playerc import *

from numpy import matrix
from numpy import linalg
import numpy as np
from pylab import *
from matplotlib import pyplot as plt

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
#print 'Robot size: (%.3f,%.3f)' % (p.size[0], p.size[1])

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

# Make a function that reads inputs
def read():
	if c.read() == None:
		raise playerc_error_str()

# Create matrix that is all grey
n = 20 # For an n x n matrix // For the 1.22 m stage, n = 122 places it in the limits
r = 10 #"resolution
a = matrix( zeros([n,n])) #this matrix has all values filled
			# with '0,' the value of grey
rg = 0.3 # Range of the sonars

# Setting up the figure where the map is displayed
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)


# Need a first read for all others to work
read()

while 1:
    read()
    x = int(r*p.px)
    y = int(r*p.py)
#    for i in range((x-2),(x+3)):
 #       for j in range((y-2),(y+3)):
    a[ int(n/2 - y), int(n/2 + x)] = -1
    if s.scan[0] < rg:
        ang = p.pa - 15*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[1] < rg:
        ang = p.pa - 45*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[2] < rg:
        ang = p.pa - 90*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[3] < rg:
        ang = p.pa - 150*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[4] < rg:
        ang = p.pa + 150*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[5] < rg:
        ang = p.pa + 90*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[6] < rg:
        ang = p.pa + 45*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[0]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
       # if (Rx > 121) | (Ry > 121):
        #    break
        a[ int(Ry), int(Rx) ] = 1
    if s.scan[7] < rg:
        ang = p.pa + 15*math.pi/180
        x = r*p.px
        y = r*p.py
        h = s.scan[7]
        Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
        Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
        a[ int(Ry), int(Rx) ] = 1

    ax.matshow(a, cmap=cm.binary, vmin=-1, vmax=1)
    plt.draw() #show

# Clean up
p.unsubscribe()
s.unsubscribe()
c.disconnect()
