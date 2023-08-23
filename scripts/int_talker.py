#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class Talker():
    def __init__(self):
        self.number_pub = rospy.Publisher("/number", Int32, queue_size=10)
        self.number = 0
    
    def publish(self):
        int32 = Int32()
        int32.data = self.number
        
        self.number_pub.publish(int32)
        
        rospy.loginfo(f"Published {int32.data}")
        
        self.number += 1
        
if __name__ == "__main__":
    rospy.init_node("int_talker_node")
    
    talker = Talker()
    
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        talker.publish()
        
        rate.sleep()