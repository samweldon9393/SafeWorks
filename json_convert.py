import sqlite3
import json

conn = sqlite3.connect('./data/providers.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM providers')
rows = cursor.fetchall()

cursor.execute('PRAGMA table_info(providers)')
columns = [column[1] for column in cursor.fetchall()]

data = [dict(zip(columns, row)) for row in rows]

with open('providers.json', 'w') as f:
    json.dump(data, f, indent=4)

conn.close()
