#!/usr/bin/env python3

import rospy
#from ros_practice_msgs.srv import AddTwoInt
from mypkg.srv import AddTwoInt

class Client():
    def __init__(self):
        self.client = rospy.ServiceProxy("/addtwoint", AddTwoInt)
        
    def call(self, x, y):
        rospy.wait_for_service("/addtwoint")
        
        res = self.client(x, y)
        
        return res

if __name__ == "__main__":
    rospy.init_node("addtwoint_client_node")
    
    client = Client()
    
    x = int(input("xの値は? -> "))
    y = int(input("yの値は? -> "))
    
    rospy.loginfo(f"Requesting x = {x} y ={y}")
    
    res = client.call(x, y)
    
    rospy.loginfo(f"Response z = {res.z}")