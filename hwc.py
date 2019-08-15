import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
import csv

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

GPIO.add_event_detect(pin, GPIO.RISING)

turns = int(sys.argv[1])
turns_now = -1 

def my_callback(channel):

    global turns
    turns += 1
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' turns = {}'.format(turns))

GPIO.add_event_callback(pin, my_callback)

def write_to_csv(time_now, turns_now):
    line = [time_now.strftime("%Y-%m-%d %H:%M:%S"), str(turns_now)]
    filename = "hamster_" + time_now.strftime("%Y%m%d") + ".csv"
    with open(filename, mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(line)

print("Counting started at {}".format(datetime.now()))

while True:
    time_now = datetime.now()
    if turns_now != turns:
        turns_now = turns
        write_to_csv(time_now, turns_now)
        time.sleep(10)
