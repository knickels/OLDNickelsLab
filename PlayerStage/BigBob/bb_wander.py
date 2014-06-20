import sys, os,math
sys.path.append('/usr/local/lib64/python2.6/site-packages/')

from playerc import *


# Create a client object
c = playerc_client(None, 'localhost', 6665)
#c = playerc_client(None, 'localhost', 6675)

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
# (sonar is for stage-3, ranger for stage-4)
s = playerc_sonar(c,0)

if s.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise ValueError(playerc_error_str())

# Retrieve the geometry
if s.get_geom() != 0:
  raise playerc_error_str()

#print 'Sonar pose: (%.3f,%.3f,%.3f)' % (s.poses.px,s.poses.py,s.poses.pz)


# start going forware
p.set_cmd_vel(0.2, 0.0, 00.0 * math.pi / 180.0, 1)

clear_dist = 2;

if c.read() == None:
  raise playerc_error_str()

while (1):
  if c.read() == None:
    raise playerc_error_str()

  min_dist =2.0;
  if s.scan_count>0:
		  sonarscanstr = 'Sonar scan: '
		  for j in range(0,s.scan_count):
					 sonarscanstr += '%.3f ' % s.scan[j]
					 if s.scan[j] < min_dist:
								min_dist = s.scan[j]
		  print sonarscanstr

		  print "space fwd = %.3f" % min_dist

  if min_dist<1.0:
		  p.set_cmd_vel(0.0, 0.0, 20.0*math.pi/180.0, 1)
  else:
		  p.set_cmd_vel(0.2, 0.0, 00.0 * math.pi / 180.0, 1)

# Clean up
p.unsubscribe()
l.unsubscribe()
c.disconnect()
