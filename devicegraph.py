import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel files
file1 = pd.read_csv("AQM00002_.csv")
file2 = pd.read_csv("AQM00003_.csv")

# Columns to compare
columns_to_compare = ['TEMPERATURE', 'HUMIDITY', 'FLOW', 'TSP', 'PM10']

# Assuming 'RECIEVED TIME' is the column containing date and time
date_time_column = 'RECIEVED TIME'

# Extract date from 'RECIEVED TIME' and create dynamic date groups
file1[date_time_column] = pd.to_datetime(file1[date_time_column])
file2[date_time_column] = pd.to_datetime(file2[date_time_column])

min_date = min(file1[date_time_column].min(), file2[date_time_column].min())
# print(min_date)
max_date = max(file1[date_time_column].max(), file2[date_time_column].max())
# print(max_date)

date_groups = pd.date_range(start=min_date, end=max_date, freq='2D').strftime('%d')
# print(date_groups)

ddg = []
for date in date_groups:
    groupdate = str(date) + "-" + str(int(date)+1)
    ddg.append(groupdate)

print(ddg)
# Iterate through each parameter
for column in columns_to_compare:
    # Create lists to store average values for each device
    device1_data = []
    device2_data = []

    # Split data into groups for each device
    for date_group in date_groups:
        group_start_date = (pd.to_datetime(date_group) - pd.DateOffset(days=1)).strftime('%m-%d')
        group_end_date = pd.to_datetime(date_group).strftime('%m-%d')

        group_data_device1 = file1[
            (file1[date_time_column].dt.strftime('%m-%d') >= group_start_date) &
            (file1[date_time_column].dt.strftime('%m-%d') <= group_end_date)
        ][column].mean()

        group_data_device2 = file2[
            (file2[date_time_column].dt.strftime('%m-%d') >= group_start_date) &
            (file2[date_time_column].dt.strftime('%m-%d') <= group_end_date)
        ][column].mean()

        device1_data.append(group_data_device1)
        device2_data.append(group_data_device2)

    # Plot the graph for the current parameter
    plt.figure()
    plt.plot(date_groups, device1_data, label='Device 1')
    plt.plot(date_groups, device2_data, label='Device 2')

    # Customize the plot
    plt.xlabel('Date Range')
    plt.ylabel(f'Average {column} Value')
    plt.title(f'Comparison of {column} for Device 1 and Device 2')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

# Show all the plots
# plt.show()
