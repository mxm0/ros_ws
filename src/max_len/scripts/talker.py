#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
import time
PI = 3.1415926535897

pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=1)
rospy.init_node('talker', anonymous=True)
cmd_vel = Twist()
time.sleep(1)

def mv_straight(speed):
    cmd_vel.linear.x = speed
    cmd_vel.angular.z = 0
    rospy.loginfo(cmd_vel)
    pub.publish(cmd_vel)
    time.sleep(1)

def turn_cw(angle):
    cmd_vel.linear.x = 0
    cmd_vel.angular.z = -(angle * 2 * PI/360)	
    rospy.loginfo(cmd_vel)
    pub.publish(cmd_vel)
    time.sleep(1)

def turn(angle): 
    cmd_vel.linear.x = 0
    cmd_vel.angular.z = angle * 2 * PI/360
    rospy.loginfo(cmd_vel)
    pub.publish(cmd_vel)
    time.sleep(1)

def talker():
    rate = rospy.Rate(10) #10Hz
    while not rospy.is_shutdown():    
	mv_straight(1)
	turn(135)
	mv_straight(1.5)
	turn(-135)
	mv_straight(1)
	turn(135)
	mv_straight(0.75)
	turn(90)
	mv_straight(0.75)
	turn(45)
	mv_straight(1)
	turn(135)
	mv_straight(1.5)
	turn(-135)
	mv_straight(1)
        rospy.wait_for_service('/reset')
        reset = rospy.ServiceProxy('/reset', Empty)
        reset()
        time.sleep(1)
        rate.sleep()
    
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
