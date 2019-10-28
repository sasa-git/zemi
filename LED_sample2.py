import RPi.GPIO as GPIO
import time

LED_OUT = 15
INPUT = 2

#callback関数の定義                                                                                           
def switch_callback(gpio_pin):
    print(gpio_pin)
    GPIO.output(LED_OUT, GPIO.HIGH)

GPIO.setmode(GPIO.BCM)  #GPIOへアクセスする番号をBCMの番号で指定することを宣言します。                        
GPIO.setup(LED_OUT, GPIO.OUT) #BCMの15番ピン、物理的には10番ピンを出力に設定します。                                
GPIO.setup(INPUT, GPIO.IN)   #BCM 2番ピンを入力に設定します。                                                      

GPIO.add_event_detect(INPUT, GPIO.FALLING, bouncetime=100)
GPIO.add_event_callback(INPUT, switch_callback) #スイッチ入力端子の状態ををcallbackのトリガとして指定します。     

try:
    while True:
        GPIO.output(LED_OUT, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()
