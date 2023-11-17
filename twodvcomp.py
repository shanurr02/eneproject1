import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel files
file1 = pd.read_csv("AQM00002_.csv")
file2 = pd.read_csv("AQM00003_.csv")

# Columns to compare
columns_to_compare = ['TEMPERATURE', 'HUMIDITY', 'FLOW', 'TSP', 'PM10']

# Assuming 'RECORDED TIME' is the column containing dates
date_column = 'RECORDED TIME'

# Group by dates and calculate the average for each parameter
for column in columns_to_compare:
    # Combine data from both files for the current column
    combined_data = pd.concat([file1[[date_column, column]], file2[[date_column, column]]])

    # Convert the date column to datetime format
    combined_data[date_column] = pd.to_datetime(combined_data[date_column])

    # Group by every 2 days and calculate the average
    grouped_data = combined_data.groupby(pd.Grouper(key=date_column, freq='2D')).mean().reset_index()

    # Plot the graph for the current parameter
    plt.figure()
    plt.plot(grouped_data[date_column], grouped_data[column], label='Average ' + column)
    
    # Customize the plot
    plt.xlabel('Date')
    plt.ylabel('Average Value')
    plt.title('Average ' + column + ' Over Time')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()

# Show all the plots
plt.show()
