#!/usr/bin/python3
import os
import time
from amplifier_config import amplifiers
from datetime import datetime
import csv

if not os.path.exists('Rides'):
    os.mkdir('Rides')

filename = datetime.now().strftime('Rides/Ride_%Y.%m.%d.csv')


with open(filename, 'a', newline='') as csvfile:
    field_names = ['Date', 'Time'] + list(amplifiers.keys())
    writer = csv.DictWriter(csvfile, fieldnames=field_names)

    csv_row = {'Date': time.strftime("%d/%m/%Y", time.localtime(time.time())),
                'Time': time.strftime("%H:%M", time.localtime(time.time()))}

    for key, value in amplifiers.items():
        try:
            amplifier = value["board"](value["spi"], value["cs"])
            temp_c = amplifier.temperature
            print(key, f": {temp_c}{chr(176)}C")
            csv_row[key] = temp_c
        except RuntimeError as cyl_rte:
            print(key, ":", cyl_rte)
        time.sleep(2.0)
    writer.writerow(csv_row)
    # print(csv_row)
