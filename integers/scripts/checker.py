#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    print(msg.data)

rospy.init_node('checker')
sub = rospy.Subscriber('oddeven', String, callback)

rospy.spin()