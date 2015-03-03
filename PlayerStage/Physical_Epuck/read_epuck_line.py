# example of use of a serial port in python
# from pyserial.sourceforge.net/shortintro.html

import sys,os
sys.path.append('/usr/local/lib64/python2.6/site-packages/')
sys.path.append('/usr/local/lib64/python2.7/site-packages/')

import serial
ser = serial.Serial('/dev/rfcomm3',115200,timeout=1)
x = ser.readline() # clear out welcome message if necc
print 'read', x
cmd = "m\n"
for i in range(20):
    nw = ser.write(cmd)
    if nw != len(cmd):
        print 'wrote %d bytes, not %d - %s' % (nw,len(cmd),cmd)
    # get response
    x = ser.readline()
    # print 'read', x
    str = x.split(','); # m,lsensor,csensor,rsensor,0,0
    sensor = int(str[2]); # use only center sensor for now
    print 'center sensor = %d' % sensor

ser.close()
