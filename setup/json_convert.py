import sqlite3
import json

conn = sqlite3.connect('./data/providers.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM providers')
rows = cursor.fetchall()

cursor.execute('PRAGMA table_info(providers)')
columns = [column[1] for column in cursor.fetchall()]

data = []

for row in rows:
    row_dict = dict(zip(columns, row))

    if row_dict['hours']:
        try:
            hours_str = row_dict['hours'].strip('"').replace("'", '"').replace("None", "null")
            row_dict['hours'] = json.loads(hours_str)
        except (json.JSONDecodeError, SyntaxError) as e:
            print(f"Error parsing 'hours' for row {row_dict['id']}: {e}")
            row_dict['hours'] = None
    else:
        row_dict['hours'] = None

    data.append(row_dict)

with open('providers.json', 'w') as f:
    json.dump(data, f, indent=4)

conn.close()
