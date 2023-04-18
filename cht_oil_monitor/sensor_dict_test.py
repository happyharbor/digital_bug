#!/usr/bin/python3
import time
from amplifier_config import amplifiers


def flow():
    for key, value in amplifiers.items():
        try:
            amplifier = value["board"](value["spi"], value["cs"])
            temp_c = amplifier.temperature
            print(key, f": {temp_c}{chr(176)}C")
        except RuntimeError as cyl_rte:
            print(key, ":", cyl_rte)
        time.sleep(2.0)


while True:
    flow()

