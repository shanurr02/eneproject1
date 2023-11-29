from datetime import datetime, timedelta
from turtle import st
import requests
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.text import Annotation

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
# timestamps = []
def get_24_hour_intervals(data, recorded_time):
    intervals = []
    start_time = recorded_time[0]
    # print(start_time)
    end_time = start_time + timedelta(hours=7)
    # print(end_time)
    interval_data = {}
    for key in data:
        if key != "recorded_time" and key != "recieved_time":
            values = data[key]
            interval_values = [value for time, value in zip(recorded_time, values) if start_time <= time < end_time and value is not None and value != "null" and value != None]
            if interval_values:
                # print(interval_values)
                interval_data[key] = round(sum(interval_values) / len(interval_values), 3)
                # print(interval_data)
            else:
                interval_data[key] = None
    intervals.append(interval_data)
    start_time = end_time
    # print(start_time)
    for i in range(13):
        end_time = start_time + timedelta(days=0.5)
        # print(end_time)
        interval_data = {}
        for key in data:
            if key != "recorded_time" and key != "recieved_time":
                values = data[key]
                interval_values = [value for time, value in zip(recorded_time, values) if start_time <= time < end_time and value is not None and value != "null" and value != None]
                if interval_values:
                    print(interval_values , end_time, key)
                    interval_data[key] = round(sum(interval_values) / len(interval_values), 3)
                else:
                    interval_data[key] = None
        intervals.append(interval_data)
        start_time = end_time
    flag = False
    # print(datetime.now())
    # print(end_time)
    if datetime.now().hour > 19:
        flag = True
    if flag:
        start_time = end_time
        end_time = recorded_time[-1]
        interval_data = {}
        for key in data:
            if key != "recorded_time"and key != "recieved_time":
                values = data[key]
                interval_values = [value for time, value in zip(recorded_time, values) if start_time <= time < end_time and value is not None and value != "null" and value != None]
                if interval_values:
                    interval_data[key] = round(sum(interval_values) / len(interval_values), 3)
                else:
                    interval_data[key] = None
        intervals.append(interval_data)
    return intervals
    
def get_time_intervals(recorded_time):
    # Sort the recorded times
    # recorded_time.sort()
    intervals = []

    # First interval from 12 midnight to 7 in the morning
    start_time = recorded_time[0]
    end_time = start_time.replace(hour=7, minute=0, second=0)
    intervals.append({"start": start_time, "end": end_time})

    # 13 consecutive intervals from 7 in the morning to 7 in the evening
    for i in range(13):
        start_time = end_time
        end_time = start_time + timedelta(hours=12)
        intervals.append({"start": start_time, "end": end_time})

    # Last interval from 7 in the evening to 12 am midnight
    start_time = end_time
    end_time = start_time.replace(hour=0, minute=0, second=0) + timedelta(days=1)
    intervals.append({"start": start_time, "end": end_time})
    # print(intervals)
    return intervals

def getrequest(id):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()

    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/6"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response

def find_day(date):
    # Assuming 'date' is a datetime object
    day_string = date.strftime("%A")
    return day_string

def getdatabyweek(id):
    json_response = getrequest(id)
    recorded_time = json_response["recorded_time"]
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        "flow": (0.9, 1.1)
    }
    
    # Filter the data
    filtered_data = filter_data(json_response, value_ranges)
    # Get 12-hour intervals
    data_intervals = get_24_hour_intervals(filtered_data, recorded_time)
    
    # # Rearrange the output to the desired format
    output_format = {key: [interval_data[key] for interval_data in data_intervals] for key in data_intervals[0]}
    values_lists = list(output_format.values())
    for key, average_values in output_format.items():
        print(f"{key}: {average_values}")
    # Create a 2D matrix
    matrix = []
    for values_list in values_lists:
        matrix.append(values_list)

    # print(matrix)

    return matrix, recorded_time

def plot_3d_scatter(x, y, z, title, intervals):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Filter out None values
    valid_indices = [i for i in range(len(z)) if z[i] is not None]
    x = [x[i] for i in valid_indices]
    y = [y[i] for i in valid_indices]
    z = [z[i] for i in valid_indices]
    intervals = [intervals[i] for i in valid_indices]

    # Plot the points
    sc = ax.scatter(x, y, z, c='blue', marker='o')

    # Create hover labels
    labels = [f"{point} - {interval}" for point, interval in zip(z, intervals)]
     # Create a dummy annotation to support hover
    label = ax.annotate('', xy=(0, 0), xytext=(20, 20), textcoords='offset points',
                        bbox=dict(boxstyle='round', edgecolor='w', facecolor='w'),
                        arrowprops=dict(arrowstyle='->', edgecolor='w', facecolor='w'))

    # Create a dummy annotation to support hover
    def update_position(e):
        sc.set_offsets(e)
        pos = ax.transData.transform(e)  # Adjusted to transData
        label.xy = pos

    def hover(event):
        vis = label.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                # Fix: Extract the index correctly
                ind = ind['ind'][0] if 'ind' in ind else None

                if ind is not None:
                    update_position(sc.get_offsets()[ind])
                    label.set_text(labels[ind])
                    label.set_visible(True)
                    fig.canvas.draw_idle()
            else:
                if vis:
                    label.set_visible(False)
                    fig.canvas.draw_idle()

    # Attach hover events
    fig.canvas.mpl_connect('motion_notify_event', hover)

    # Set labels
    ax.set_xlabel('Temperature')
    ax.set_ylabel('Humidity')
    ax.set_zlabel(title)

    plt.title(f'{title} vs Temperature and Humidity')
    plt.show()

def main():
    matrix, recorded_time = getdatabyweek("03")
    temperature = matrix[0]
    humidity = matrix[1]
    tsp = matrix[3]
    pm1 = matrix[4]
    pm2_5 = matrix[5]
    pm10 = matrix[6]
    intervals = get_time_intervals(recorded_time)

    # Plotting
    plot_3d_scatter(temperature, humidity, pm1, 'PM1', intervals)
    # plot_3d_scatter(temperature, humidity, pm2_5, 'PM2_5', intervals)
    # plot_3d_scatter(temperature, humidity, pm10, 'PM10', intervals)
    # plot_3d_scatter(temperature, humidity, tsp, 'tsp', intervals)
if __name__ == "__main__":
    main()
