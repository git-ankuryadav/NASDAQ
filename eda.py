import pandas as pd

data = pd.read_csv('Dataset/data.csv', index_col=0)
data['Date'] = pd.to_datetime(data['Date'])

data['OnlyDate'] = data['Date'].dt.date
data['OnlyTime'] = data['Date'].dt.time

print("Min Date:", data['OnlyDate'].min())
print("Max Date:", data['OnlyDate'].max())
print("Range:", data['OnlyDate'].max() - data['OnlyDate'].min())







