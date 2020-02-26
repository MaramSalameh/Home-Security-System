import RPi.GPIO as GPIO
import time
import picamera
GPIO.setmode(GPIO.BCM)
sensor = 2
GPIO.setup(sensor, GPIO.IN)

cam = picamera.PiCamera()
#p_state = False
#c_state = False
#current_state = sensor 
try:
    time.sleep(.1)
    while True: 
        if GPIO.input(sensor):
            cam.start_preview()
#    if c_state != p_state:
 #       if c_state:
  #          cam.start_preview()
        else: 
            cam.stop_preview()
GPIO.cleanup()
