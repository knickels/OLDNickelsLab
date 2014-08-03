#!/usr/bin/python
import math

def dtor (deg):
    return deg*math.pi/180.0;
    

"------------------------------------------------------------------------"
" Main Executable when called as a script. "
if __name__ == "__main__":

# Define states
    s_fwd = 1;       # Move forward
    s_spinL = 2;     # Spin counter clockwise
    s_spinR = 3;     # Spin clockwise


# Constants to be used in script
    rg = 0.07; # Max range the ir can sense
    m_vel = 0.1; #Epuck max speed: 13cm/s
    #   For 13cm/s max speed, max turn in degree/s:
    m_spinR = -100;        # Spin clockwise: -201.3
    m_spinL = 100;         # Spin counter clockwise: +201.3



# playerc is the python interface to player & stage
    import sys, os
    sys.path.append('/usr/local/lib/python2.7/site-packages/')
    sys.path.append('/usr/local/lib64/python2.6/site-packages/')
    from playercpp import *

    from numpy import matrix
    from numpy import linalg
    import numpy as np
    from pylab import *
    from matplotlib import pyplot as plt

    robot = PlayerClient("localhost");

    # Retrieve the geometry
    pp = Position2dProxy(robot,0);
    pp.RequestGeom()
    size = pp.GetSize()
    print 'Robot size: (%.3f,%.3f,%.3f)' % (size.sw, size.sl, size.sh)

    # create a proxy for ir:0
    ir = IrProxy(robot,0);

# Create matrix that is all grey
    n = 180 # For an n x n matrix // For the 1.22 m stage, n = 122 places it in the limits
    r = 100 #"resolution
    m = matrix( zeros([n,n])) #this matrix has all values filled
                        # with '0'
    m = m + 0.5    # Sets all values to 0.5, "grey"
    rg = 0.07 # Range of the sonars

# Angle offsets for each sensor
    t = [-math.pi/12, -math.pi/4, -math.pi/2, -5*math.pi/6, 5*math.pi/6, math.pi/2, math.pi/4, math.pi/12]

# Setting up the figure where the map is displayed
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ind = 0

    while(1):
        ind += 1
        # read from the proxies
        robot.Read()

        px = pp.GetXPos()
        py = pp.GetYPos()
        pa = pp.GetYaw()

        X = int(r*px)
        Y = int(r*py)
        x = r*px
        y = r*py
        a = pa
        if ir.GetCount()<8:
          hy = [ 0.7,0.7,0.7,0.7,0.7,0.7,0.7,0.7]
	else:
          hy = [ ir.GetRange(0), ir.GetRange(1), ir.GetRange(2), ir.GetRange(3), ir.GetRange(4), ir.GetRange(5), ir.GetRange(6), ir.GetRange(7) ]

# epuck IR
#  7 0
# 6   1
# 5   2
#  4 3

# Setting 5 x 5 square white where the E-puck is currently at
        for i in range((X-2),(X+3)):
            for j in range((Y-2),(Y+3)):
                m[ int(n/2 - j), int(n/2 + i)] = 0

        for i in range(0, 8):
            ang = a + t[i]
            h = hy[i]
    # Occupied 
            if hy[i] < rg:
                Rx = n/2 + x + r*h*math.cos(ang) + 0.032*r*math.cos(ang) #The last bit is to account for the epuck radius
                Ry = n/2 - (y + r*h*math.sin(ang) + 0.032*r*math.sin(ang)) #The last bit is to account for the epuck radius
                m[ int(Ry), int(Rx) ] = 1
    # Probably empty
            for j in range(0, int(1000*h)):
                Rx = n/2 + x + j*r*h*math.cos(ang)/110 + 0.032*r*math.cos(ang)
                Ry = n/2 - (y + j*r*h*math.sin(ang)/110 + 0.032*r*math.sin(ang))
                if m[ int(Ry), int(Rx) ] == 1:
                    m[ int(Ry), int(Rx) ] = 1
                else:
                    m[ int(Ry), int(Rx) ] *= 0.9

        if ind%10 == 0:
            ax.matshow(m, cmap=cm.binary, vmin=0, vmax=1)
            plt.draw() #show
