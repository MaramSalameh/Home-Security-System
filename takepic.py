import os, sys, time, datetime, picamera
import RPi.GPIO as GPIO

def PIR_detection(sensor):
    if (GPIO.input(sensor) == True):
        return True
    else:
        return False
    
def main():
    pir_sensor = 23
    # gpio pin on rpi set to input
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pir_sensor, GPIO.IN)
    while True:
        time.sleep(0.1)
        if PIR_detection(pir_sensor) == True:
            os.system("""raspistill -o /path/to/picture.jpg""")
            os.system("""uuencode picture.jpg picture.jpg| mail -s \"You know this cat?!\" user@gmail.com""")
            time.sleep(15)

            
main()
