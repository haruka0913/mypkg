#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class Talker():
    def __init__(self):
        self.text_pub = rospy.Publisher("/text", String, queue_size=10)
        
    def publish(self):
        string = String()
        string.data = "Hello world"
        
        self.text_pub.publish(string)
        
        rospy.loginfo(f"Published{string.data}")
    
if __name__ == "__main__":
    rospy.init_node("talker_node")
    
    talker = Talker()
    
    rate = rospy.Rate(15)
    
    while not rospy.is_shutdown():
        talker.publish()
        
        rate.sleep()
