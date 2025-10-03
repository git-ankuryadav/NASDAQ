import pandas as pd

ids = ['03-24', '03-25', '06-24', '06-25', '09-25', '12-24']

all_data = []  # To store data from all files

for id in ids:
    # Use f-string instead of wrong string interpolation
    data1 = pd.read_csv(f"Dataset/MNQ {id}.csv")
    
    # Split Date and Time
    # data1[['Date', 'Time']] = data1['Date'].str.split(' ', expand=True)
    data1['Date'] = pd.to_datetime(data1['Date'], format='%Y%m%d %H%M%S')
    # data1['Time'] = pd.to_datetime(data1['Time'], format='%H%M%S').dt.time
    
    # Select relevant columns
    # data1 = data1[['Date', 'Time', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    # Append to the list
    all_data.append(data1)

# Concatenate all dataframes vertically
combined_data = pd.concat(all_data, ignore_index=True)

# Save combined data to CSV (append=False overwrites file)
combined_data.to_csv("Dataset/data.csv")


