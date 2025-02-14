import numpy as np
import pandas as pd 
import re

def split_days(string):
    split = re.split(r'[;,\s]', string)
    for i, s in enumerate(split):
        if s == '':
            continue
        else:
            print(s)
#df = pd.read_csv('./providers_2.csv')

#hours = df['hours']

test = "Mon, Wed, Fri 1 pm 4 pm; Tue 9 am 4 pm; Thu 1 pm 6 pm"
print(split_days(test))

