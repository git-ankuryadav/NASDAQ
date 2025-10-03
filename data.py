import pandas as pd

ids = ['03-24', '03-25', '06-24', '06-25', '09-25', '12-24']

all_data = []  

for id in ids:

    data1 = pd.read_csv(f"Dataset/MNQ {id}.csv")   
    data1['Date'] = pd.to_datetime(data1['Date'], format='%Y%m%d %H%M%S')
    all_data.append(data1)


combined_data = pd.concat(all_data, ignore_index=True)
combined_data.to_csv("Dataset/data.csv")


