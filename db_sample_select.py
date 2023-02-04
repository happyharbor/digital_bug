import psycopg2

try:
    conn = psycopg2.connect("dbname='bug' user='postgres' host='localhost' password='postgres'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute("""SELECT * from temperature""")

rows = cur.fetchall()

print("\nShow me the temperatures:\n")
for row in rows:
    str_row = ""
    for column in row:
        str_row = str_row + f" ${column}"
    print(str_row)
