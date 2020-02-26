import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN)

sensor = 27

while True:
    if GPIO.input(sensor) == 0:
        print('unlatched')
        time.sleep(time until notified)
        if GPIO.input(sensor) == 0:
            os.system("""echo \"The door is open\" | mail -s \"Door is unlatched!\" phonenumber@txt.att.net""")
    else:
        print('latched')
GPIO.cleanup()
