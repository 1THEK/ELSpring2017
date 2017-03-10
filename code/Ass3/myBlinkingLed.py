#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import signal


def signal_handler(signal, frame):
	"""Function to handle the quiting of the program. Ctrl-C Catch"""
	print "Deallocating resources"
	GPIO.cleanup()
	sys.exit(0)

def Blink(t):
	"""Function to blink for t time delay"""
	GPIO.output(24,True) #Turn LED on
	time.sleep(t) # Wait t seconds
	GPIO.output(24,False) # Turn LED off

#Init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
signal.signal(signal.SIGINT,signal_handler)

while True:
	#Three Blinks 
	for x in range(3):
		Blink(0.5)
		time.sleep(0.5)
	time.sleep(5) # Wait 5 seconds
	# Four fast Blinks
	for x in range(4):
		Blink(0.5)
		time.sleep(0.5)
	#Wait 5 seconds
	time.sleep(5)


GPIO.cleanup()
