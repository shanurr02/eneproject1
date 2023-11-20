from datetime import datetime, timedelta
import requests
import matplotlib.pyplot as plt


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


def split_data_by_weeks(recorded_time, data):
    if len(recorded_time) != len(data["temperature"]):
        raise ValueError("Mismatched lengths of recorded_time and data lists")

    start_time = min(recorded_time)
    end_time = max(recorded_time)

    # Calculate the number of days between start and end
    num_days = (end_time - start_time).days

    midpoint = start_time + timedelta(days=num_days // 2)

    week1_data = {key: [] for key in data}
    week2_data = {key: [] for key in data}

    for time, temp, hum, pm1, pm2_5, pm5, pm10, tsp in zip(recorded_time, data["temperature"], data["humidity"], data["PM1"], data["PM2_5"], data["PM5"], data["PM10"], data["TSP"]):
        if time <= midpoint:
            week1_data["temperature"].append(temp)
            week1_data["humidity"].append(hum)
            week1_data["PM1"].append(pm1)
            week1_data["PM2_5"].append(pm2_5)
            week1_data["PM5"].append(pm5)
            week1_data["PM10"].append(pm10)
            week1_data["TSP"].append(tsp)
        else:
            week2_data["temperature"].append(temp)
            week2_data["humidity"].append(hum)
            week2_data["PM1"].append(pm1)
            week2_data["PM2_5"].append(pm2_5)
            week2_data["PM5"].append(pm5)
            week2_data["PM10"].append(pm10)
            week2_data["TSP"].append(tsp)


    return week1_data, week2_data

def calculate_averages(data):
    averages = {}
    for key, values in data.items():
        averages[key] = round(sum(values) / len(values), 3) if values else None
    return averages

def get_24_hour_intervals(data, recorded_time):
    intervals = []
    start_time = recorded_time[0]
    for i in range(7):
        end_time = start_time + timedelta(days=1)
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
    # data_intervals = get_24_hour_intervals(json_response, recorded_time)
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
    pm1 = matrix[5]
    pm2_5 = matrix[6]
    pm10 = matrix[7]
    tsp = matrix[4]
    # Plotting
    plot_3d_scatter(temperature, humidity, pm1, 'PM1')
    plot_3d_scatter(temperature, humidity, pm2_5, 'PM2.5')
    plot_3d_scatter(temperature, humidity, pm10, 'PM10')
    plot_3d_scatter(temperature, humidity, tsp, 'TSP')

main()
# if __name__ == "__main__":
#     getdatabyweek()
        # Read the token from the file
    # with open("token.txt", "r") as f:
    #     tk = f.read().strip()


    # get_url = "https://api.thingzcloud.com/devices/getData/AQM00003/7"
    # header = {
    #     "x-api-key": tk
    # }
    # get_response = requests.get(get_url, headers=header)
    # json_response = get_response.json()

    # recorded_time = json_response["recorded_time"]
    # recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # # Get 12-hour intervals
    # data_intervals = get_24_hour_intervals(json_response, recorded_time)
    
    # # Rearrange the output to the desired format
    # output_format = {key: [interval_data[key] for interval_data in data_intervals] for key in data_intervals[0]}

    # # Print the output
    # for key, average_values in output_format.items():
    #     print(f"{key}: {average_values}")
