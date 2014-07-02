import math
import numpy as np
def dtor (deg):
    return deg*math.pi/180.0;
n=100
X_p= x*np.ones(N)    #Define the vector of particles
Y_p= y*np.ones(N)


import sys, os
# this should be whereever "playercpp.py" is.  
# On linux, you can find this out with "locate playercpp.py"
sys.path.append('/usr/local/src/player-3.0.2/build/client_libs/libplayerc++/bindings/python/')
from playercpp import *


# Make proxies for Client, Ranger, Position2d, Simulation
robot1 = PlayerClient("localhost");
rp1 = RangerProxy(robot1,0);
pp1 = Position2dProxy(robot1,0);
sp1= SimulationProxy(robot1,0)
gp1= Graphics2dProxy(robot1)
#This is only needed if there are multiple robots on seperate ports
robot2 = PlayerClient("localhost", 6666);
rp2 = RangerProxy(robot2,0);
pp2 = Position2dProxy(robot2,0);


while(1):
    # read from the proxies
    robot1.Read()
    robot2.Read()
  

    # sometimes you miss a scan, just start over
    if rp1.GetRangeCount() < 8 and rp2.GetRangeCount() <8:
        continue;
    # print out rangers, for fun
  
    for i in range(N):
        X_p[i] = X_p[i]+X+math.sqrt(V_1)*np.random.randn(1,1)  #Normalized data around initial conidtion
        Y_p[i] = Y_p[i]+Y+math.sqrt(V_2)*np.random.randn(1,1)
  
#    rangerstr1="Ranger scan 1: "
#    rangerstr2="Ranger scan 2: "
#    for i in range(rp1.GetRangeCount()):
#         x=rp1.GetRange(i)
#	 rangerstr1 += '%.3f ' % x 
#    print rangerstr1

    #Get the location and bearing of each E-Puck


    pp1.RequestGeom()
    x,y,theta= pp1.GetXPos(), pp1.GetYPos(), pp1.GetYaw()
    print("X Location:  %.2f  Y Location:  %.2f Bearing:  %.2f" %(x,y,theta))



#    for i in range(rp2.GetRangeCount()):
#         y=rp2.GetRange(i)
#	 rangerstr2 += '%.3f ' % y 
#    print rangerstr2

#    pp2.RequestGeom()
#    print pp2.GetXPos(), pp2.GetYPos(), pp2.GetYaw(),

    
    #Moving the second epuck to the loction of particles    

    sp1.SetPose2d("epuck_2",x,y,theta)    



 # do simple collision avoidance
#    short = 0.09;
 #   small = 0.09;
  #  if rp.GetRange(0) < short or rp.GetRange(7) < short:
   #   speed = 0.0;
  #  elif rp.GetRange(1) <0.06 or rp.GetRange(6)< 0.06:
   #   speed = 0.05
  #  else:
  #    speed = 0.100;
  #  if rp.GetRange< short or rp.GetRange(6)<short or rp.GetRange(7)<short:
  #    turnrate = dtor(-30); # turn 20 degrees per second
  #  elif rp.GetRange(0)<short or rp.GetRange(1)<short:
  #    turnrate = dtor(30);
  #  elif rp.GetRange(2)<small :
  #    turnrate = dtor(45);
  #  elif rp.GetRange(5)<small:
  #    turnrate = dtor(-45);
  #  else:
  #    turnrate = 0;
  #  pp.SetSpeed(speed, turnrate);


    position2d
    
    
   
    
