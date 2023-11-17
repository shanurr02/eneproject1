import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel files
file1 = pd.read_csv("AQM00002_.csv")
file2 = pd.read_csv("AQM00003_.csv")

# Columns to compare
columns_to_compare = ['TEMPERATURE', 'HUMIDITY', 'FLOW', 'TSP', 'PM10']

# Assuming 'RECIEVED TIME' is the column containing date and time
date_time_column = 'RECIEVED TIME'

# Extract date from 'RECIEVED TIME' and create groups of two consecutive days
file1[date_time_column] = pd.to_datetime(file1[date_time_column])
file2[date_time_column] = pd.to_datetime(file2[date_time_column])

date_groups = pd.date_range(start='2023-10-24', end='2023-11-16', freq='2D').strftime('%m-%d').tolist()
print(date_groups)
# Iterate through each parameter
for column in columns_to_compare:
    # Create lists to store average values for each device
    device1_data = []
    device2_data = []

    # Split data into groups for each device
    for date_group in date_groups:
        group_data_device1 = file1[(file1[date_time_column].dt.strftime('%m-%d') == date_group)][column].mean()
        group_data_device2 = file2[(file2[date_time_column].dt.strftime('%m-%d') == date_group)][column].mean()

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
plt.show()
