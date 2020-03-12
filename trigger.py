# Libraries
import RPi.GPIO as GPIO
import time

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24

# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


def get_distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

button_pressed = False
button_pressed_before = False

while True:
    distance = get_distance()
    if distance <= 1:
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