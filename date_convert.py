import numpy as np
import pandas as pd 
import re

days = {
        "Mon" : "Monday",
        "Tue" : "Tuesday",
        "Wed" : "Wednesday",
        "Thu" : "Thursday",
        "Fri" : "Friday",
        "Sat" : "Saturday",
        "Sun" : "Sunday" 
        }
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
    split = re.split(r'[;,\s]+', string)
    i = 0
    while i < len(split):
        queue = []
        times = []
        while split[i] in days:
            queue.append(split[i])
            i += 1
        if split[i].isnumeric():
            if split[i + 1] == 'pm':
                times.append(int(split[i]) + 12)
            else:
                times.append(int(split[i]))
            if split[i + 3] == 'pm':
                times.append(int(split[i + 2]) + 12)
            else:
                times.append(int(split[i + 2]))
            i += 4
        for day in queue:
            hours[days[day]] = times.copy()
        i += 1

    print(hours)



#df = pd.read_csv('./providers_2.csv')

#hours = df['hours']

test = "Mon, Wed, Fri 1 pm 4 pm"
#; Tue 9 am 4 pm; Thu 1 pm 6 pm"
print(split_days(test))

