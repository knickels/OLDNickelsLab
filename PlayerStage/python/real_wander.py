# Author: Pablo Tarquino (building off of Eric Kang's work)
# This code allows a robot with sonars to "wander" a stage world.
# This is the basic wander module,
# It will react simply upon seeing an obstacle
import sys
import os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

import math
from playerc import *


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
#if p.get_geom() != 0:
#  raise playerc_error_str()
# print 'Robot size: (%.3f,%.3f)' % (p.size[0], p.size[1])

# Create a proxy for sonar:0
# (laser is for stage-3, ranger for stage-4)
s = playerc_ir(c,0)
if s.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise playerc_error_str()

# Retrieve the geometry
if s.get_geom() != 0:
  raise playerc_error_str()

# (pose changed format from stage-3 to stage-4)
#print 'Sonar pose: (%.3f,%.3f,%.3f)' % (l.pose[0],l.pose[1],l.pose[2])
#print 'Laser pose: (%.3f,%.3f,%.3f)' % (l.device_pose.px,l.device_pose.py,l.device_pose.pz)

#E-puck constants
#   Epuck max speed: 13 cm/s
m_vel = 0.13
#   For 13cm/s max speed, max turn in degree/s:
mturn_cw = -201.3
mturn_ccw = 201.3

#p.set_cmd_vel( 0.0 , 0.0, 100.0 * math.pi / 180.0, 1)
p.set_cmd_vel( 0.0 , 0.0, 0.0 * math.pi / 180.0, 1)

# Needs a first read before it will read any other.
if c.read() == None:
  raise playerc_error_str()

while 1:
  if c.read() == None:
    raise playerc_error_str()

  if s.data.ranges_count > 7:
	print s.data.ranges


  if s.data[1] !=0:
  #if (s.scan[7] < 0.1) | (s.scan[6] < 0.08) | (s.scan[5] < 0.04): #Spin CW
    p.set_cmd_vel(0.0, 0.0, -100 * math.pi / 180.0, 1) #should be mturn_cw
  elif (s.scan[0] < 0.1) | (s.scan[1] < 0.08) | (s.scan[2] < 0.04): #Spin CW
    p.set_cmd_vel(0.0, 0.0, mturn_ccw * math.pi / 180.0, 1)
  else:
    p.set_cmd_vel( 0.8*m_vel, 0.0, 0.0 * math.pi / 180.0, 1)

# Clean up
p.unsubscribe()
s.unsubscribe()
c.disconnect()
