import numpy as np
import pandas as pd

def split_address_notes(string):
    strings = string.split('[')
    if len(strings) == 1:
        return [string, None]
    if string[-1] == ']':
        addr = strings[0][:-1]
        note = strings[1][:-1]
    else:
        split = strings[1].split(']')
        note = split[0]
        addr = strings[0] + split[1]
    return addr, note 

def split_addr_col(col):
    new_col = []
    for string in col:
        new_col.append(split_address_notes(string))
    return new_col


df = pd.read_csv('./providers.csv')
#print(df['address'])
new_col = split_addr_col(df['address'])
new_df = pd.DataFrame(new_col)

df['address'] = new_df[0]
df['address note'] = new_df[1]

df.to_csv('providers_2.csv')
