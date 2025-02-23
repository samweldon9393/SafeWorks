import numpy as np
import pandas as pd
import sqlite3
import json

conn = sqlite3.connect('./data/providers.db')

#cursor.execute('PRAGMA table_info(providers)')
#res = cursor.fetchall()
#print(res)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS providers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    address TEXT,
    phone TEXT,
    hours TEXT,
    note TEXT
)
''')


#cursor.execute('''
#INSERT INTO providers5 (id, name, address, phone, hours, note)
#SELECT "Unnamed: 0.1", name, address, "phone number", hours, "address note" FROM providers;
#''')

cursor.execute('DROP TABLE providers')
cursor.execute('ALTER TABLE providers5 RENAME TO providers')

conn.commit()
conn.close()
