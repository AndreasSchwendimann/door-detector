from gpiozero import DistanceSensor
from time import sleep

event_url = 'www.panda-cuddles.ch/api/Event'

def get_distance():
    sensor = DistanceSensor(echo=11, trigger=7)
    return (sensor.distance * 100)

door_status = False
door_status_before = False

while True:
    distance = get_distance()
    if distance <= 1:
        print("++ button was pressed")
        door_status = True
    else:
        print("-- no button was pressed")
        door_status = False

    if door_status and not door_status_before:
        requests.post(event_url, json={'created': str(datetime.datetime.now()), 'location': 'office 1', 'action': 'open'})
    if not door_status and door_status_before:
        requests.post(event_url, json={'created': str(datetime.datetime.now()), 'location': 'office 1', 'action': 'close'})

    door_status_before = door_status
    sleep(1)