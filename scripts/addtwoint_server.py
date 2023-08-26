#!/usr/bin/env python3

import rospy
#from ros_practice_msgs.srv import AddTwoInt, AddTwoIntResponse
from mypkg.srv import AddTwoInt, AddTwoIntResponse

class Server():
    def __init__(self):
        self.addint_srv = rospy.Service("/addtwoint", AddTwoInt, self.callback)
        
    def callback(self, req):
        rospy.loginfo(f"Recived x = {req.x} y = {req.y}")
        
        res = AddTwoIntResponse()
        res.z = req.x + req.y
        
        rospy.loginfo(f"Sending z = {res.z}")
        
        return res
    
if __name__ == "__main__":
    rospy.init_node("addtwoint_server_node")
    
    server = Server()
    
    rospy.spin()