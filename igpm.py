import pandas as pd

df = pd.read_excel('relatorio-igpm.xlsx')

df['RecordDate'] = pd.to_datetime(df['RecordDate'], unit='s')

df['Year'] = df['RecordDate'].dt.year
df['Month'] = df['RecordDate'].dt.month

counts = df.groupby(['Year', 'Month']).size()

print(counts)
