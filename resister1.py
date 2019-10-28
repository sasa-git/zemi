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
    
    GPIO.output(rclk, HIGH)
    GPIO.output(rclk, LOW)

SER = 25
RCLK = 24
SRCLK = 23

GPIO.setmode(GPIO.BCM) # GPIOへアクセスする番号をBCMの番号で指定することを宣言します。
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)

LEDdata1 = [1, 1, 0]
LEDdata2 = [1, 0, 1]
LEDdata3 = [0, 1, 1]

try:
    while True:
        sendLEDdata(LEDdata1, SER, RCLK, SRCLK)
        sleep(1)
        sendLEDdata(LEDdata2, SER, RCLK, SRCLK)
        sleep(1)
        sendLEDdata(LEDdata3, SER, RCLK, SRCLK)
        sleep(1)

# Ctrl+C を押すことで、例外 KeyboardInterrupt が発生→except ~~ でその例外を補足、pass でWhile処理を抜ける
except KeyboardInterrupt:
    pass

GPIO.cleanup()
