import pandas as pd

fp = 'RDC.csv'  # this is the csv file from the main source
data = pd.read_csv(fp)
nj_data = data[data['county_name'].str.contains(", nj", case=False, na=False)]
nj_data.to_csv('nj_data.csv', index=False)
