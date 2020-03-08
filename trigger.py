import RPi.GPIO as GPIO
import time
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

event_url = 'http://www.panda-cuddles.ch/api/Event'
session_url = 'http://www.panda-cuddles.ch/api/Session'

button_pressed_before = False
button_pressed = False

while True:
    if GPIO.input(10) == GPIO.HIGH:
        print("++ button was pressed")
        button_pressed = True
    else:
        print("-- no button was pressed")
        button_pressed = False

    if button_pressed and not button_pressed_before:
        requests.post(event_url, json={'created': str(datetime.datetime.now()), 'location': 'office 1', 'action': 'open'})
    if not button_pressed and button_pressed_before:
        requests.post(event_url, json={'created': str(datetime.datetime.now()), 'location': 'office 1', 'action': 'close'})

    button_pressed_before = button_pressed
    time.sleep(1)