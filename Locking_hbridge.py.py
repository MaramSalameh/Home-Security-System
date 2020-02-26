import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
Motor1A = 16
Motor1B = 20
Motor1E = 21
 
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
pwm1A = GPIO.PWM(Motor1A, 250)
pwm1B = GPIO.PWM(Motor1B, 250)
pwm1A.start(0)
pwm1B.start(0)

print "Going forwards"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)
pwm1A.ChangeDutyCycle(50)
time.sleep(2)
 
print "Going backwards"
GPIO.output(Motor1A,GPIO.LOW)
GPIO.output(Motor1B,GPIO.HIGH)
GPIO.output(Motor1E,GPIO.HIGH)
pwm1B.ChangeDutyCycle(100)
time.sleep(2)
 
print "Now stop"
GPIO.output(Motor1E,GPIO.LOW)

pwm1A.stop()
pwm1B.stop()
GPIO.cleanup()
