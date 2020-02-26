import os, picamera, sys, time
import RPi.GPIO as GPIO
import subprocess

LOCAL_DIRECTORY = "/home/pi/captured_images"

def generate_file_name():
	return time.strftime("%Y-%m-%d-%H-%M-%S-%Z", time.localtime())


def PIR_detection(sensor):
    if (GPIO.input(sensor) == True):
        return True
    else:
        return False

def take_snapshot(filename):
    camera.capture(get_file_name())


def main():
    pir_sensor = 23
    cam = picamera.PiCamera()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_sensor, GPIO.IN)
    
    filename = LOCAL_DIRECTORY + generate_file_name()
    while True:
        time.sleep(0.1)
        if PIR_detection(pir_sensor) == True:
            camera.capture(filename)
            # next: send email with image attachment
       
main()
