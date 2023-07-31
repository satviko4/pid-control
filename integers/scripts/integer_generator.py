#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

rospy.init_node('integer_generator')
pub = rospy.Publisher('integers', Int32, queue_size=10)
rate = rospy.Rate(2)
while not rospy.is_shutdown():
    pub.publish(random.randint(0, 1000))
    rate.sleep()
    