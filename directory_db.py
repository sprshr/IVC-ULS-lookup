from bs4 import BeautifulSoup
from directory_html import directory
import sqlite3 as sq

doc = BeautifulSoup(directory, 'html.parser')
conn = sq.connect('directory.db')
cursor = conn.cursor()
try:
    cursor.execute('''CREATE TABLE directory(
        name TEXT,
        title TEXT,
        department TEXT,
        division TEXT,
        workSpace TEXT,
        phone TEXT
    )
    ''')
except sq.OperationalError:
    raise Exception("Database Already Exists")
count = 1
for child in doc.div.children:
    count = count * -1
    if count < 0:
        continue
    name = child.div.div.h2.a.text
    title = ""
    department = ""
    division = ""
    work_space = ""
    phone = ""
    for header in child.div.find_all('div')[1].ul.find_all('li'):
        if header.small is not None:
            text = header.small.text
            text = text.split(": ")
            if text[0] == "Title":
                title = text[1]
            elif text[0] == "Department":
                department = text[1]
            elif text[0] == "Division":
                division = text[1]
            elif text[0] == "Work Space":
                word_space = text[1]
            elif text[0] == "Phone":
                phone = text[1]
    with conn:
        cursor.execute(f'''INSERT INTO directory VALUES (
            "{name}",
            "{title}",
            "{department}",
            "{division}",
            "{work_space}",
            "{phone}"
        )''')
    print(name, title, department, division, work_space, phone)

conn.close()
print("Directory Database Create")