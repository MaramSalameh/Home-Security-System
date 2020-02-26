"""
This program will control various sensors connected to the raspberry pi
and alert the user through email or sms.

Sonoma State University, Capstone project

Author: Maram Salameh.

Date: 
"""

import sys, time, picamera
from Adafruit_ADS1x15 import ADS1x15
import RPi.GPIO as GPIO

 ###### initialize/set variables #######   
ads1015 = 0x00
GPIO.setmode(GPIO.BCM)

###### code to control piezo sensor ####### 
    # initialize adc with default mode
adc = ADS1x15(ic=ads1015)
while True:
    reading = adc.readADCSingleEnded(3, 1024, 860)
    print(round(reading, 6))
time.sleep(0.01)

##### code to control hall effect sensor #####
GPIO.setmode(GPIO.BCM)
hall_sensor = # pin connected to rpi gpio


#### motion detection code #####
pir_pin = 7
GPIO.setup(pir_pin, GPIO.IN)
while True:
    if GPIO.input(pir_pin):
        return True
    else:
        return False
