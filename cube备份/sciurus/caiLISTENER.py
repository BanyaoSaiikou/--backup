#!/usr/bin/env python
# coding: utf-8

import rospy
from visualization_msgs.msg import MarkerArray

def callback(data):
    # Print the received MarkerArray message
    rospy.loginfo("Received MarkerArray message:")
    i=0
    for marker in data.markers:
      
        rospy.loginfo(i)
        rospy.loginfo("Marker position: x={}, y={}, z={}".format(marker.pose.position.x+0.14979217, marker.pose.position.y+0.02789325, marker.pose.position.z+0.57816425))#for 1280x1080
        print("------------")
        i+=1
        if i==0:
            blue_cube=[0,marker.pose.position.x+0.14979217, marker.pose.position.y+0.02789325, marker.pose.position.z+0.57816425]
        elif i==1:
            bottom_space=[1,marker.pose.position.x+0.14979217, marker.pose.position.y+0.02789325, marker.pose.position.z+0.57816425]
        elif i==2:
            top_left_knob=[2,marker.pose.position.x+0.14979217, marker.pose.position.y+0.02789325, marker.pose.position.z+0.57816425]
        

def listener():
    # Initialize ROS node
    rospy.init_node('listener', anonymous=True)

    # Subscribe to the "/sciurus17/example/my_object" topic
    rospy.Subscriber("/sciurus17/example/my_object", MarkerArray, callback)

    # Spin to keep the script from exiting
    rospy.spin()

if __name__ == '__main__':
    listener()

