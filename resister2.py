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

INPUT_SWITCH = 2

GPIO.setmode(GPIO.BCM) # GPIOへアクセスする番号をBCMの番号で指定することを宣言します。
GPIO.setup(SER, GPIO.OUT)
GPIO.setup(RCLK, GPIO.OUT)
GPIO.setup(SRCLK, GPIO.OUT)
GPIO.setup(INPUT_SWITCH, GPIO.IN)

LED_data_list = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

try:
    while True:
        if GPIO.input(INPUT_SWITCH) == GPIO.LOW:
            for LEDdata in LED_data_list:
                sendLEDdata(LEDdata, SER, RCLK, SRCLK)
                sleep(1)
        else:
            sendLEDdata([0,0,0], SER, RCLK, SRCLK)

# Ctrl+C を押すことで、例外 KeyboardInterrupt が発生→except ~~ でその例外を補足、pass でWhile処理を抜ける
except KeyboardInterrupt:
    pass

GPIO.cleanup()
