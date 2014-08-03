#!/usr/bin/env python

import roslib; roslib.load_manifest('rospy_tutorials')
import rospy
import re
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D, PoseStamped
class RoomDetail():
  def _init_(self, room, x, y, theta):
    self.x=x
    self.y=y
    self.theta=theta

def parser(filename):
  f=open(filename,'rU')
  i=0
  r={}
  f_lines=f.readlines()
  for line_raw in f_lines:
    l=re.search('.+',line_raw)
    line=l.group()
    if i%4==0:
      room=(line)
      i=i+1
    elif i%4==1:
      x_temp=(line)
      i=i+1
    elif i%4==2:
      y_temp=(line)
      i=i+1
    elif i%4==3:
      theta_temp=(line)
      r[room]=room+','+x_temp+','+y_temp+','+theta_temp
      del room
      del x_temp
      del y_temp
      del theta_temp
      i=i+1
    if i==len(f_lines)-1:
	    f.close()
  return r

def talker(init_room,fin_room, r):
  pub_init = rospy.Publisher('initialpose', Pose2D)
  rospy.init_node('talker', anonymous=True)
  init_loc=Pose2D()
  rt=rospy.Rate(1)
  init_room_detail=(r[init_room]).split(',')
  init_loc.x=float(init_room_detail[1])
  init_loc.y=float(init_room_detail[2])
  init_loc.theta=float(init_room_detail[3])
  count=0
  while count < 5: 
    pub_init.publish(init_loc)
    rospy.loginfo(init_loc)
    count=count+1
    rt.sleep()
"""
  fin_room_detail=(r[fin_room]).split(',')
  pub_fin=rospy.Publisher('move_base_simple/goal', PoseStamped)
  fin_loc=PoseStamped()
  fin_loc.header.frame_id='map'
  fin_loc.pose=Pose(Point(float(fin_room_detail[1]),float(fin_room_detail[2]),0), Quaternion(0,0,0,float(fin_room_detail[3],0)))
  count=0
  while count < 5:
    pub_fin.publish(fin_loc)
    rospy.loginfo(fin_loc)
    count=count+1
    rt.sleep()
"""

def main():
  filename='/home/nnararid/catkin_ws/src/csi_navigation/scripts/ListOfRooms'
  r={}
  r=parser(filename)
  init_room=raw_input('Where are you?')
  fin_room=raw_input('Where do you want to go?')
  talker(init_room,fin_room,r)
  
            
if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException: pass
