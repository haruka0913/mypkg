#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class Listener():
    def __init__(self):
        self.text_sub = rospy.Subscriber("/number", Int32, self.callback)
        
    def callback(self, msg):
        
        number = msg.data * 2
        
        rospy.loginfo(f"Subscribed {number}")
    
if __name__ == "__main__":
    rospy.init_node("int_listener_node")
    
    listener = Listener()
    
    rospy.spin()