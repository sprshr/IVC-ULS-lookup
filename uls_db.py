import sqlite3 as sq
try:
    conn = sq.connect('uls.db')
    cursor = conn.cursor()
    cursor.execute(''' CREATE TABLE uls(
        callSign Text,
        name TEXT,
        city TEXT,
        state TEXT,
        zipCode TEXT
    )
    ''')
except sq.OperationalError:
    raise Exception("Database Already Exists")
with open('l_amat/EN.dat','r') as data:
    for row in data:
        operator = row.split("|")
        call_sign = operator[4]
        name = operator[8].replace("\"", "'") + " " + operator[10].replace("\"", "'")
        city = operator[16]
        state = operator[17]
        zip_code = operator[18]
        with conn:
            try:
                cursor.execute(f""" INSERT INTO uls VALUES(
                    "{call_sign}",
                    "{name}",
                    "{city}",
                    "{state}",
                    "{zip_code}"
                )
                """)
                print(call_sign, name, city, state, zip_code)
            except(sq.OperationalError):
                with open("uls.log", 'a') as log:
                    log.write(f"Error {call_sign}")
    conn.close()