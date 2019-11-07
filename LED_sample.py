import RPi.GPIO as GPIO
import time

LED_OUT = 15
# INPUT = 18
INPUT = 2 # 2ピンは常にHIGHとなっている

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_OUT, GPIO.OUT)
GPIO.setup(INPUT, GPIO.IN)

try:
    while True:
        if GPIO.input(INPUT) == GPIO.LOW:
            GPIO.output(LED_OUT, GPIO.HIGH)
        else:
            GPIO.output(LED_OUT, GPIO.LOW)
        
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
