#!/usr/bin/env python
#!coding:utf-8
#基于人体红外传感器和蜂鸣器的树莓派报警器
#Author: Jiahui Tang
#Time: 2016-12-09

#import the necessary packages
import RPi.GPIO as GPIO
import time

#set the mode of the GPIO of raspberrypi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN)
GPIO.setup(11,GPIO.OUT,initial=GPIO.HIGH)

#main loop
while True:
	while GPIO.input(12):
			GPIO.output(11,GPIO.LOW)
	GPIO.output(11,GPIO.HIGH)

#clean
GPIO.cleanup()	
