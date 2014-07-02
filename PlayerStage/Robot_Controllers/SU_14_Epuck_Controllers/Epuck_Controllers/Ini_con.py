import math

def dtor (deg):
    return deg*math.pi/180.0;
    
import sys, os
# this should be whereever "playercpp.py" is.  
# On linux, you can find this out with "locate playercpp.py"
sys.path.append('/usr/local/src/player-3.0.2/build/client_libs/libplayerc++/bindings/python/')
from playercpp import *

# Make proxies for Client, Sonar, Position2d
robot = PlayerClient("localhost");
sp = SonarProxy(robot,0);
pp = Position2dProxy(robot,0);

while(1):
    # read from the proxies
    robot.Read()

    # sometimes you miss a scan, just start over
    if sp.GetCount() < 8:
        continue;

    # print out sonars, for fun
    sonarstr="Sonar scan: "
    for i in range(sp.GetCount()):
        sonarstr += '%.3f ' % sp.GetScan(i)
    print sonarstr


     # do simple collision avoidance
    short = 0.5;
    if sp.GetScan(0) < short or sp.GetScan(2)<short:
      turnrate = dtor(-20); # turn 20 degrees per second
    elif sp.GetScan(1) <short or sp.GetScan(3)<short:
      turnrate = dtor(20);
    else:
      turnrate = 0;

    if sp.GetScan(0) < short or sp.GetScan(1) < short:
      speed = 0;
    else:
      speed = 0.100;

    # command the motors
    pp.SetSpeed(speed, turnrate);
