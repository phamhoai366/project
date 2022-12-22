#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback_laser(msg):


  regions=[min(min(msg.ranges[0:102]) , 2),
    min(min(msg.ranges[102:205]) , 2),
    min(min(msg.ranges[205:307]) , 2),
    min(min(msg.ranges[308:410]) , 2),
    min(min(msg.ranges[411:513]) , 2),
    min(min(msg.ranges[514:617]) , 2),
    min(min(msg.ranges[618:719]) , 2)]

  print(regions)


  rospy.loginfo(regions)


def main():
  rospy.init_node('reading_laser')
  sub= rospy.Subscriber("/scan", LaserScan, callback_laser)

  rospy.spin()

if __name__ == '__main__':
  main()

