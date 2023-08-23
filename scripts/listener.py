#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Listener():
    def __init__(self):
        self.text_sub = rospy.Subscriber("/text", String, self.callback)
        
    def callback(self, msg):
        rospy.loginfo(f"Subscribed {msg.data}")
            
if __name__ == "__main__":
    rospy.init_node("listener_node")
    
    listener = Listener()
    
    rospy.spin()