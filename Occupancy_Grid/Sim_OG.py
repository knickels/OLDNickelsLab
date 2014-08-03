# Author: Pablo Tarquino (building off of Eric Kang's work)
# First "real-time" mapping program.
# Notes: It needs external program to operate robot (playerv, etc.)
#      Improvement: Make faster response time
#      Improvement: Make continuous plotting, not just when it changes direction

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
n = 165 # For an n x n matrix // For the 1.22 m stage, n = 122 places it in the limits
r = 100 #"resolution
m = matrix( zeros([n,n])) #this matrix has all values filled
			# with '0'
m = m + 0.5    # Sets all values to 0.5, "grey"
rg = 0.1 # Range of the sonars

# Angle offsets for each sensor
t = [-math.pi/12, -math.pi/4, -math.pi/2, -5*math.pi/6, 5*math.pi/6, math.pi/2, math.pi/4, math.pi/12]

# Setting up the figure where the map is displayed
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)


# Need a first read for all others to work
read()
ind = 0
while 1:
    ind +=1
    read()
    X = int(r*p.px)
    Y = int(r*p.py)
    x = r*p.px
    y = r*p.py
    a = p.pa
    hy = [ s.scan[0], s.scan[1], s.scan[2], s.scan[3], s.scan[4], s.scan[5], s.scan[6], s.scan[7] ]

# Setting 5 x 5 square white where the E-puck is currently at
    for i in range((X-2),(X+3)):
        for j in range((Y-2),(Y+3)):
            m[ int(n/2 - j), int(n/2 + i)] = 0

    for i in range(0, 8):
        ang = a + t[i]
        h = hy[i]
        if hy[i] < rg:
            Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
            Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
            m[ int(Ry), int(Rx) ] = 1
        for j in range(0, int(1000*h)): 
            Rx = n/2 + x + j*r*h*math.cos(ang)/110 + 0.032*r*math.cos(ang)
            Ry = n/2 - (y + j*r*h*math.sin(ang)/110 + 0.032*r*math.sin(ang))
            if m[ int(Ry), int(Rx) ] == 1:
                m[ int(Ry), int(Rx) ] = 1
            else:
                m[ int(Ry), int(Rx) ] = 0

    if ind%10 == 0:
        ax.matshow(m, cmap=cm.binary, vmin=0, vmax=1)
        plt.draw() #show

# Clean up
p.unsubscribe()
s.unsubscribe()
c.disconnect()
