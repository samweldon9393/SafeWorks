import numpy as np
import pandas as pd 
import re
import sqlite3
import json

days = {
        "Mon" : "Monday",
        "Tue" : "Tuesday",
        "Wed" : "Wednesday",
        "Thu" : "Thursday",
        "Fri" : "Friday",
        "Sat" : "Saturday",
        "Sun" : "Sunday" 
        }

day_list = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

hours_template = {
        "Monday" : None,
        "Tuesday" : None,
        "Wednesday" : None,
        "Thursday" : None,
        "Friday" : None,
        "Saturday" : None,
        "Sunday" : None,
        }

def split_days(string):


    hours = hours_template.copy()

    if "Please" in string:
        for day in hours:
            hours[day] = "Please call"
        return hours

    string = string.replace(":", "")
    split = re.split(r'[;,\s]+', string)
    i = 0
    

    while i < len(split):
        queue = []
        times = []
            
        while split[i] in days:
            queue.append(split[i])
            if split[i + 1] == "through":
                for j in range(day_list.index(split[i]) + 1, day_list.index(split[i + 2]) + 1):
                    queue.append(day_list[j])
                i += 3 
            else:
                i += 1
        if split[i].isnumeric():
            if split[i + 1] == 'pm':
                if int(split[i]) < 13:
                    times.append(int(split[i]) + 12)
                else:
                    times.append(int(split[i]) + 1200)

            else:
                times.append(int(split[i]))
            if split[i + 3] == 'pm':
                if int(split[i + 2]) < 13:
                    times.append(int(split[i + 2]) + 12)
                else:
                    times.append(int(split[i + 2]) + 1200)
            else:
                times.append(int(split[i + 2]))
            i += 3
        for day in queue:
            hours[days[day]] = times.copy()
        i += 1

    return hours

def convert_col(col):
    new_col = []
    for string in col:
        new_col.append(split_days(string))
    return new_col




df = pd.read_csv('./providers_4.csv')

#hours = df['hours']
#df['hours'] = convert_col(df['hours'])
df['hours'] = df['hours'].apply(json.dumps)

conn = sqlite3.connect('providers.db')

df.to_sql("providers", conn, if_exists="replace", index=False)
conn.close()

'''
df.to_csv('providers_4.csv')
test = "Mon, Wed, Fri 1 pm 4 pm; Tue 9 am 4 pm; Thu 1 pm 6 pm"
test2 = "Mon, Tue, Thu 9 am 1 pm; Fri 1 pm 7 pm"
test3 = "Wed 10 am 3 pm"
test4 = "Mon through Fri 10:30 am 5:30 pm"
test5 = "Thu Please Call"
print(split_days(test))
print(split_days(test2))
print(split_days(test3))
print(split_days(test4))
print(split_days(test5))
'''
