import RPi.GPIO as GPIO
from datetime import datetime

REED_PIN = 12
GPIO.setmode(GPIO.BCM)
WATER_COUNTER = 0.0
WATER_10L = 0.0

def reed_contact(channel):
    global WATER_COUNTER
    global WATER_10L
    WATER_COUNTER = WATER_COUNTER + 0.5
    WATER_10L = WATER_10L + 0.5
    print(datetime.now()," Water consumed: ",WATER_COUNTER)
    
GPIO.setup(REED_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(REED_PIN, GPIO.FALLING, callback=reed_contact, bouncetime=50)

while True:
    if WATER_10L > 10:
        WATER_10L = 0
        print("10 liters consumed!")

GPIO.cleanup()
