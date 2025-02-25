import numpy as np
import pandas as pd
import sqlite3
import json

conn = sqlite3.connect('./data/providers.db')

df = pd.read_sql("SELECT * from providers", conn)


conn.close()

#df['hours'] = df['hours'].apply(json.loads)

print(nodup)
