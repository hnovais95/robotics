#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

def callback(msg):
    print(msg)

rospy.init_node("topic_subscriber")
sub = rospy.Subscriber('/(nosso_topico)/angulo_juntas', JointState, callback)
rospy.spin()