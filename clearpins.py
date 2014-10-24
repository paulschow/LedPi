# A small script to reset the GPIO PWM pins for the LED

#import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# set up GPIO output channels
GPIO.setup(28, GPIO.OUT)  # Green
GPIO.setup(29, GPIO.OUT)  # Red
GPIO.setup(30, GPIO.OUT)  # Blue

# Green LED at pin 28, 500 Hz
G = GPIO.PWM(28, 60)
# Start off
G.start(100)
R = GPIO.PWM(29, 60)
R.start(100)
B = GPIO.PWM(30, 60)
B.start(100)
#try:
    #while 1:
        #p.ChangeDutyCycle(0)
    ##while 1:
        ##for dc in range(0, 101, 5):
            ##p.ChangeDutyCycle(dc)
            ##time.sleep(0.1)
        ##for dc in range(100, -1, -5):
            ##p.ChangeDutyCycle(dc)
            ##time.sleep(0.1)
#except KeyboardInterrupt:
    #pass

R.stop()
G.stop()
B.stop()
GPIO.cleanup()
