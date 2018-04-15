#!/bin/env python
#encording: utf-8
import unittest, rostest
import rosnode, rospy
import time
from pimouse_ros.msg import MortorFreqs
from geometry_msgs.msg import Twist

class MotorTest(unittest.TestCase):
	def file_check(self,dev, value,message):
		with open("/dev/" +dev,"r") as f:
			self.assertEqual(f.readline(), str(value)+"\n", message)
	def test_node_exist(self):
		nodes=rosnode.get_node_names()
		self.assertIn('/motors', nodes, "node does not exist")
	def test_put_freq(self):
		pub=rospy.Publisher('/motor_raw', MotorFreqs)
		m=MotorFreqs()
	 	m.left_hz=123
		m.right_hz=456
		for i in range(10):
			pub.publish(m)
			time.sleep(0.1)
		self.file_check("rtmotor_raw_l0", m.left_hz, "wrong left value from motor_raw")
		self.file_check("rtmotor_raw_r0", m.right_hz, "wrong right value from motor_raw")

	def test_put_cmd_vel(self):
		pub=rospy.publisher('/cmd_vel', Twist)
		m=Twist()
		m.linear.x=0.1414
		m.angular.z=1.57
		for i in range(10):
			pub.publish(n)
			time.sleep(0.1)
		self.file_check("rtmotor_raw_l0", 200 , "wrong left value from cmd_vel")
		self.file_check("rtmotor_raw_r0", 600 , "wrong write value from cmd_vel")

		time.sleep(1.1)
		self.file_check("rtmotor_raw_l0", 0 , "dont stop after 1[s]")
		self.file_check("rtmotor_raw_r0", 0 , "dont stop after 1[s]")

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node('travis_test_mortors')
	rostest.rosrun('pimouse_ros', 'travis_test_mortors', MortorTest)

