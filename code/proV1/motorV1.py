#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import random
from collections import defaultdict

GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.OUT)
times =defaultdict(int)

def run(t):
	GPIO.output(24,True)
	time.sleep(times[t])
	GPIO.output(24,False)

def init_Dict():
	for x in range(10):
		times[x] = x
	

init_Dict()
run(3)
GPIO.cleanup()
