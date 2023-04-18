import psycopg2

conn = psycopg2.connect("dbname='bug' user='postgres' host='localhost' password='postgres'")

cur = conn.cursor()

cur.execute("""INSERT INTO measurement (type) VALUES ('temperature') RETURNING id""")

measurement_id = cur.fetchone()[0]

postgres_insert_query = """ INSERT INTO temperature (measurement_id, source, temperature) VALUES (%s,%s,%s)"""
record_to_insert = (measurement_id, 'Cyl1', 50)
cur.execute(postgres_insert_query, record_to_insert)

conn.commit()
