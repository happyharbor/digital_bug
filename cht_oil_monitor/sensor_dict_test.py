# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time

from amplifier_config import amplifiers


def flow():
    temperatures = []
    while len(temperatures) < len(amplifiers):
        for name, value in amplifiers.items():
            try:
                amplifier = value["board"](value["spi"], value["cs"])
                temp_c = amplifier.temperature
                print(name, ": {} C".format(temp_c))
            except RuntimeError as cyl_rte:
                print(name, ":", cyl_rte)
            time.sleep(1.0)


while True:
    flow()

