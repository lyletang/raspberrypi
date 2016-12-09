#!/usr/bin/env python
#!coding:utf-8
#树莓派b+对HC-SR04超声波测距传感器的使用
#Author: Jiahui Tang
#Time: 2016-12-09

#import the necessary packages
import RPi.GPIO as GPIO
import time

#define the function of check the distance
def checkdist():
	GPIO.output( 11, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output( 11, GPIO.LOW)
	while not GPIO.input(12):
		pass
	t1 = time.time()
	while GPIO.input(12):
		pass
	t2 = time.time()
	
	#return the distance
	return (t2-t1) * 340 / 2

#set the mode of the GPIO of raspberrypi
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(12, GPIO.IN)

#ready
time.sleep(2)

#main
try:
	#main loop
	while True:
		#print the format distance
		print 'Distance: %0.2f m' %checkdist()

		#time delay
		time.sleep(3)

except KeyboardInterrupt:
	#clean
	GPIO.cleanup()
	
