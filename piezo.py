import time, sys, os
from Adafruit_ADS1x15 import ADS1x15

ADS1015 = 0x00  # 12-bit ADC

adc = ADS1x15(ic=ADS1015)

while 1:
  # To read channel 3 in single-ended mode, +/- 1.024V, 860 sps use:
  volts = adc.readADCSingleEnded(3, 1024, 860)
 
 
  if volts > 0.5:
    print("{0:.2f}".format(volts / 100))
    os.system("""echo \"Someone is at the door\" | mail -s \"Knock knock!\" phonenumber@txt.att.net""")
  time.sleep(0.01)
