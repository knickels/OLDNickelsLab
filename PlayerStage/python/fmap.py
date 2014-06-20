# Author: Pablo Tarquino (building off of Eric Kang's work)
# In this code a robot will wander and map its surroundings
import sys
import os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

import math
from playerc import *

import numpy as np
from pylab import *

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
n = 122 # For an n x n matrix // For the 1.22 m stage, n = 122 places it in the limits
np.random.seed(10)
a=np.random.randint(0,1, size=(n, n)) #this matrix has all values filled
					# with '0,' the value of grey

# Need a first read for all others to work
read()

while 1:
    read()
    a[int(n/2) - int(100*p.px)][int(n/2) - int(100*p.py)] = -1

    if s.scan[7] < 0.1:
        a[int(n/2) - 100*int(p.py + (0.037 - s.scan[7])*math.sin(p.pa + 1.87))][int(n/2) + 100*int(p.px + (0.037 + s.scan[7])*math.cos(p.pa + 1.87))] = 1

    mat=matshow(a, cmap=cm.binary, vmin=-1, vmax=1)
    colorbar(mat)
    draw() #show

# Clean up
p.unsubscribe()
s.unsubscribe()
c.disconnect()
