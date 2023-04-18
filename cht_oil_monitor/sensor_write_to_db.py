#!/usr/bin/python3
import time
import uuid

from amplifier_config import amplifiers
import psycopg2

conn = psycopg2.connect("dbname='bug' user='postgres' host='localhost' password='postgres'")

cur = conn.cursor()


def flow():
    for key, value in amplifiers.items():
        try:
            amplifier = value["board"](value["spi"], value["cs"])
            temp_c = amplifier.temperature
            # cur.execute("""INSERT INTO measurement (type) VALUES (%s)""", 'temperature')
            cur.execute("""INSERT INTO temperature (measurement_id, source, temperature) VALUES (%s, %s, %s)""",
                        (str(uuid.uuid4()), key, temp_c))
            # rows = cur.fetchall()
            conn.commit()
            count = cur.rowcount
            print(count, "Record inserted successfully into measurement table")

        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into measurement table", error)
            # print(key, f": {temp_c}{chr(176)}C")
        except RuntimeError as cyl_rte:
            print(key, ":", cyl_rte)
        time.sleep(2.0)


while True:
    flow()
