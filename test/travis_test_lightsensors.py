#!/bin/env python
#encording: utf-8
import unittest, rostest
import rosnode, rospy
import time
form pimouse_ros.msg import LightSensorValues

class LightSensorTest(unittest.TestCase):
	def setup(self):
		self.count=0
		rospy.Subscriber('/lightsensors', LighetSensorValues, self.callback)
		self.values=LightSensorValues()
	def callback(self,data):
		self.count= +=1
		self.values=data
		
	def check_values(self,lf,ls,rs,rf):
		vs=self.values
		self.asserEquel(vs.left_forword,lf, "different value: left_forword")
		self.asserEquel(vs.left_side,ls, "different value: left_side")
		self.asserEquel(vs.right_side,rs, "different value: right_side")
		self.asserEquel(vs.right_forword,rf, "different value: right_forword")
		self.asserEquel(vs.sum_all,lf+ls+rs+rf, "different value: sum_all")
		self.asserEquel(vs.sum_forword,lf+rf, "different value: sum_forword")
	def test_node_exist(self):
		nodes=rosnode.get_node_names()
		self.assertIn('/lightsensor', nodes, "node does not exost")
	def test_get_value(self):
		rospy.set_param('lightsensor_freq', 10)
		time.sleep(2)
		with open("/dev/rtlightsensor0", "w") as f:
			f.write("-1 0 123 432\n")
		time.sleep(3)
		self.assertFalse(self.count==0, "cannot subscribe the topic")
		self.check_values(4321, 123, 0, -1)
	def test_chenge_parameter(self):
		rospy.set_param('lightsensors_freq',1)
		time.sleep(2)
		c_prev=self.count
		time_sleep(3)
		self.assertTrue(self.count < c_prev + 4, "freq does not change")
		self.assertFalse(self.count == c_prev, "subscriber is stopped")

if __name__ == '__main__':
	time.sleep(3)
	rospy.init_node("travis_test_lightsensors')
	rostest.rosrun('pimouse_ros', 'travis_test_lightsensors', LightSensorTest)

