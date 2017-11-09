import pandas as pd 

from pprint import pprint

filename = "./CBD-US, CT Discrepancy.xlsx"

df = pd.read_excel(filename, sheetname="Sheet1")

print df