#!/usr/bin/env python3

import rospy
#from ros_practice_msgs.msg import Person
from mypkg.msg import Person

class Talker():
    def __init__(self):
        self.person_pub = rospy.Publisher("/person", Person, queue_size=10)
        
    def publish(self):
        msg = Person()
        msg.name = "上田 隆一"
        msg.age = 45
        msg.hobbies = ["確率ロボティクス","シェル芸"]
        
        self.person_pub.publish(msg)
        
        hobbies = f"{msg.hobbies[0]}、{msg.hobbies[1]}"
        
        rospy.loginfo(f"私は{msg.name}、{msg.age}歳！趣味は{hobbies}！")

if __name__ == "__main__":
    rospy.init_node("custom_talker_node")
    
    talker = Talker()
    
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        
        talker.publish()
    
        rate.sleep()