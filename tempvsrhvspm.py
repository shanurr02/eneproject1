from datetime import datetime, timedelta
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def filter_data(json_response, ranges):
    filtered_data = json_response.copy()
    
    for key, value_list in filtered_data.items():
        if key != "recorded_time":
            filtered_values = []
            for value in value_list:
                if value is not None:
                    if key in ranges:
                        min_range, max_range = ranges[key]
                        if min_range <= value <= max_range:
                            filtered_values.append(value)
                    else:
                        filtered_values.append(value)
            filtered_data[key] = filtered_values
    
    return filtered_data

def get_12_hour_intervals(data, recorded_time):
    intervals = []
    start_time = recorded_time[0]
    for i in range(14):
        end_time = start_time + timedelta(days=0.5)
        interval_data = {}
        for key in data:
            if key != "recorded_time":
                values = data[key]
                interval_values = [value for time, value in zip(recorded_time, values) if start_time <= time < end_time and value is not None and value != "null" and value != None]
                if interval_values:
                    interval_data[key] = round(sum(interval_values) / len(interval_values), 3)
                else:
                    interval_data[key] = None
        intervals.append(interval_data)
        start_time = end_time
    return intervals
def getrequest(id):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()


    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/7"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response


def getdatabyweek(id):
    json_response = getrequest(id)
    recorded_time = json_response["recorded_time"]
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        "flow": (0.9, 1.1)
        # Add more key-value pairs and ranges as needed
    }
    
    # Filter the data
    filtered_data = filter_data(json_response, value_ranges)
    # Get 12-hour intervals
    data_intervals = get_12_hour_intervals(filtered_data, recorded_time)
    
    # # Rearrange the output to the desired format
    output_format = {key: [interval_data[key] for interval_data in data_intervals] for key in data_intervals[0]}
    values_lists = list(output_format.values())
    for key, average_values in output_format.items():
        print(f"{key}: {average_values}")
    # Create a 2D matrix
    matrix = []
    for values_list in values_lists:
        matrix.append(values_list)

    print(matrix)

    return matrix

# getdatabyweek("03")
def plot_3d_scatter(x, y, z, title):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)

    ax.set_xlabel('Temperature')
    ax.set_ylabel('Humidity')
    ax.set_zlabel(title)

    plt.title(f'{title} vs Temperature and Humidity')
    plt.show()

def main():
    matrix = getdatabyweek("03")
    temperature = matrix[0]
    humidity = matrix[1]
    pm1 = matrix[4]
    pm2_5 = matrix[5]
    pm10 = matrix[6]
    tsp = matrix[3]
    # Plotting
    plot_3d_scatter(temperature, humidity, pm1, 'PM1')
    plot_3d_scatter(temperature, humidity, pm2_5, 'PM2.5')
    plot_3d_scatter(temperature, humidity, pm10, 'PM10')
    plot_3d_scatter(temperature, humidity, tsp, 'TSP')

main()