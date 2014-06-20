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

# Create a proxy for laser:0
# (laser is for stage-3, ranger for stage-4)
l = playerc_laser(c,0)
if l.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise ValueError(playerc_error_str())

# Retrieve the geometry
if l.get_geom() != 0:
  raise playerc_error_str()
print 'Laser pose: (%.3f,%.3f,%.3f)' % (l.pose[0],l.pose[1],l.pose[2])

# Create a proxy for sonar:0
# (sonar is for stage-3, ranger for stage-4)
s = playerc_sonar(c,0)

if s.subscribe(PLAYERC_OPEN_MODE) != 0:
  raise ValueError(playerc_error_str())

# Retrieve the geometry
if s.get_geom() != 0:
  raise playerc_error_str()

print 'Sonar pose: (%.3f,%.3f,%.3f)' % (s.poses.px,s.poses.py,s.poses.pz)


# Start the robot turning CCW at 20 deg / sec
p.set_cmd_vel(1.0, 0.0, 20.0 * math.pi / 180.0, 1)

for i in range(0,30):
  if c.read() == None:
    raise playerc_error_str()

  print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

  sonarscanstr = 'Partial sonar scan: '
  for j in range(0,s.scan_count):
    sonarscanstr += '%.3f ' % s.scan[j]
  print sonarscanstr

  laserscanstr = 'Partial laser scan: '
  for j in range(0,min(5,l.scan_count)):
    laserscanstr += '%.3f ' % l.ranges[j]
  print laserscanstr

# Now turn the other way
p.set_cmd_vel(0.0, 0.0, -20.0 * math.pi / 180.0, 1)

for i in range(0,30):
  if c.read() == None:
    raise playerc_error_str()

  print 'Robot pose: (%.3f,%.3f,%.3f)' % (p.px,p.py,p.pa)

  laserscanstr = 'Partial laser scan: '
  for j in range(0,l.scan_count):
    laserscanstr += '%.3f ' % l.ranges[j]
  print laserscanstr

# Now stop
p.set_cmd_vel(0.0, 0.0, 0.0, 1)

# Clean up
p.unsubscribe()
l.unsubscribe()
c.disconnect()
