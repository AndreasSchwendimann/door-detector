import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("++ button was pressed")
    else:
        print("-- no button was pressed")
    time.sleep(1)