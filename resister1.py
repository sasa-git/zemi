import RPi.GPIO as GPIO
from time import sleep

def sendLEDdata(data, ser, rclk, srclk):
    n = len(data)

    GPIO.output(rclk, GPIO.LOW)
    GPIO.output(srclk, GPIO.LOW)

    for i in range(n):
        if data[i] == 1:
            GPIO.output(ser, GPIO.HIGH)
        else:
            GPIO.output(ser, GPIO.LOW)
        
        GPIO.output(srclk, GPIO.HIGH)
        GPIO.output(srclk, GPIO.LOW)
    
    GPIO.output(rclk, GPIO.HIGH)
    GPIO.output(rclk, GPIO.LOW)

SER = 25
RCLK = 24
SRCLK = 23

GPIO.setmode(GPIO.BCM) # GPIOへアクセスする番号をBCMの番号で指定することを宣言します。
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)

LEDdataList = [[0,1,1], [1,0,1], [1,1,0]]

try:
    while True:
        for LEDdata in LEDdataList:
            sendLEDdata(LEDdata.reverse(), SER, RCLK, SRCLK)
            sleep(1)
        print('done!')

# Ctrl+C を押すことで、例外 KeyboardInterrupt が発生→try文内から抜ける→except KeyboardInterruptで例外を補足、例外処理に移る→pass(null operation)で例外処理は何もせずに終わる。
except KeyboardInterrupt:
    pass

GPIO.cleanup()
