import pandas as pd 

from pprint import pprint

filename = "./CBD-US, CT Discrepancy.xlsx"

df = pd.read_excel(filename, sheetname="Sheet1")

#Format Data

print df['Gender'].value_counts()
df['mean_paired_difference'] = df['cbd_us'] - df['cbd_ct']
print df.describe()