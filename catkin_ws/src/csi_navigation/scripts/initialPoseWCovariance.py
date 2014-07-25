#!/usr/bin/env python

import roslib; roslib.load_manifest('rospy_tutorials')
import rospy
import re


from std_msgs.msg import String, Header
from geometry_msgs.msg import *
def talker():
  #Initial Pose Set Up
  pub_init = rospy.Publisher('initialpose', PoseWithCovarianceStamped)
  rospy.init_node('Initial_Pose_Publish')
  initial=PoseWithCovarianceStamped()
  initial_pose=PoseWithCovariance()
  initial_pose.pose=Pose(Point(0.100,0.100,0.100),Quaternion(0.000,0.000,-0.0149,0.999))
  initial_pose.covariance=\
  [1.0,0.0,0.0,0.0,0.0,0.0,\
  0.0,1.0,0.0,0.0,0.0,0.0,\
  0.0,0.0,1.0,0.0,0.0,0.0,\
  0.0,0.0,0.0,1.0,0.0,0.0,\
  0.0,0.0,0.0,0.0,1.0,0.0,\
  0.0,0.0,0.0,0.0,0.0,1.0]
  initial.pose=initial_pose
  initial_info=Header()
  initial_info.frame_id="map"
  initial_info.stamp=rospy.Time.now()
  initial.header=initial_info
  pub_init.publish(initial)
  r=rospy.Rate(1)
  ans=str("y")

  #publishing the goal
  
  while not rospy.is_shutdown():
    rospy.loginfo("Setting Initial Pose")
    pub_init.publish(initial)
    ans=raw_input("Enter to continue") 
    rospy.loginfo("Setting Goal")

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

def main():
  filename='/home/nnararid/catkin_ws/src/csi_navigation/scripts/ListOfRooms'
  r={}
  r=parser(filename)
  init_room=raw_input('Where are you?')
  fin_room=raw_input('Where do you want to go?')
  talker(init_room,fin_room,r)
"""  
            
if __name__ == '__main__':
  try:
    talker()
  except Exception, e:
    print "error", e
