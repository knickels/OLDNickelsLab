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

    robot = PlayerClient("localhost");

    # Retrieve the geometry
    pp = Position2dProxy(robot,0);
    pp.RequestGeom()
    size = pp.GetSize()
    print 'Robot size: (%.3f,%.3f,%.3f)' % (size.sw, size.sl, size.sh)

    # create a proxy for ir:0
    ir = IrProxy(robot,0);

    state = s_fwd;

    while(1):
        # read from the proxies
        robot.Read()
        px = pp.GetXPos()
        py = pp.GetYPos()
        pa = pp.GetYaw()
        # print 'Robot pose: (%.3f,%.3f,%.3f)' % (px, py, pa)

        # print out sonars, for fun
        str="IR Sensors = "
        for i in range(ir.GetCount()):
            str += '%.2f ' % ir.GetRange(i)
        print str

# epuck IR
#  7 0
# 6   1
# 5   2
#  4 3
        if (state==s_fwd):
            print 'State = FWD\n'

            if ir.GetCount()<8:
                state = s_fwd
                continue
            elif (ir.GetRange(7) < 0.07) | (ir.GetRange(6) < 0.05): # | (ir.GetRange(5) < 0.03):
                state = s_spinR
            elif (ir.GetRange(0) < 0.07) | (ir.GetRange(1) < 0.05): # | (ir.GetRange(2) < 0.03):
                state = s_spinL
            else:
                state = s_fwd

        elif (state==s_spinR):
            print 'State = Spin Right\n'

            if ir.GetCount()<8:
                state = s_fwd
                continue
            elif (ir.GetRange(7) < 0.07) | (ir.GetRange(6) < 0.05): # | (ir.GetRange(5) < 0.03):
                state = s_spinR
            elif (ir.GetRange(0) < 0.07) | (ir.GetRange(1) < 0.05): # | (ir.GetRange(2) < 0.03):
                state = s_spinL
            else:
                state = s_fwd

        elif (state==s_spinL):
            print 'State = Spin Left\n'

            if ir.GetCount()<8:
                state = s_fwd
                continue
            elif (ir.GetRange(7) < 0.07) | (ir.GetRange(6) < 0.05): # | (ir.GetRange(5) < 0.03):
                state = s_spinR 
            elif (ir.GetRange(0) < 0.07) | (ir.GetRange(1) < 0.05): # | (ir.GetRange(2) < 0.03):
                state = s_spinL
            else:
                state = s_fwd

        else:
            print 'Error - state=%d is illegal\n' % state

        # output mapping
        if (state==s_fwd):
            turnrate = 0;
            speed = m_vel;
        elif (state==s_spinR):
            turnrate = dtor(m_spinR); # deg / sec
            speed = 0;
        elif (state==s_spinL):
            turnrate = dtor(m_spinL); # deg / sec
            speed = 0;
        else:
            turnrate = 0;
            speed = 0;
            print 'Error - state=%d is illegal\n' % state


        # command the motors
        print 'Setting speed to (%.2f,%.2f)\n'  % (speed,turnrate)
        pp.SetSpeed(speed, turnrate);

        print " "
