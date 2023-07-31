#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('oddeven_classifier')

def callback(msg):    
    isoddeven = String()
    if msg.data%2 == 0:
        isoddeven.data = "Even"
    else:
        isoddeven.data = "Odd"
    pub.publish(isoddeven)


sub = rospy.Subscriber('integers', Int32, callback)
pub = rospy.Publisher('oddeven', String, queue_size=10)
rospy.spin()
