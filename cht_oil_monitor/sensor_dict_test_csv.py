# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import os
import time
from amplifier_config import amplifiers
from datetime import datetime
import csv

if not os.path.exists('Rides'):
    os.mkdir('Rides')

starttime = time.time()
filename = datetime.now().strftime('Rides/Ride_%Y.%m.%d.csv')


def flow():
    with open(filename, 'a', newline='') as csvfile:
        field_names = ['Date', 'Time', 'Cyl 1', 'Cyl 2', 'Oil']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writerow(
            {'Date': time.strftime("%d:%m:%Y", time.localtime(time.time())),
             'Time': time.strftime("%H:%M", time.localtime(time.time()))
             })

        temperatures = []
        while len(temperatures) < len(amplifiers):
            for name, value in amplifiers.items():
                try:
                    amplifier = value["board"](value["spi"], value["cs"])
                    temp_c = amplifier.temperature
                    print(name, ": {} C".format(temp_c))
                    writer.writerow({"{}".format(temp_c)})
                except RuntimeError as cyl_rte:
                    print(name, ":", cyl_rte)
                time.sleep(2.0)


while True:
    flow()
