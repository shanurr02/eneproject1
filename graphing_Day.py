from datetime import datetime, timedelta
import requests

def find_start_time(recorded_time, end_time):
    for time in recorded_time[::-1]:
        if end_time - time > timedelta(hours=24):
            # print (time)
            return time
    return None
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

def get_hourly_averages(data, recorded_time):
    start_time = datetime.now() - timedelta(hours=24)
    hourly_averages = {key: [] for key in data if key != "recorded_time"}
    
    while start_time <= recorded_time[-1]:
        end_time = start_time + timedelta(hours=1)
        
        hour_values = {key: [] for key in data if key != "recorded_time"}
        for time, values in zip(recorded_time, zip(*[data[key] for key in data if key != "recorded_time"])):
            if start_time <= time < end_time:
                for key, value in zip(hour_values.keys(), values):
                    hour_values[key].append(value)
        
        for key in hour_values.keys():
            average_value = sum(hour_values[key]) / len(hour_values[key]) if hour_values[key] else None
            hourly_averages[key].append(average_value)
        
        start_time = end_time
    
    return hourly_averages

    
def calculate_3hourly_averages(data, recorded_time):
    start_time = datetime.now() - timedelta(hours=24)
    three_hourly_averages = {key: [] for key in data if key != "recorded_time"}
    
    while start_time <= recorded_time[-1]:
        end_time = start_time + timedelta(hours=3)
        
        three_hour_values = {key: [] for key in data if key != "recorded_time"}
        for time, values in zip(recorded_time, zip(*[data[key] for key in data if key != "recorded_time"])):
            if start_time <= time < end_time:
                for key, value in zip(three_hour_values.keys(), values):
                    three_hour_values[key].append(value)
        
        for key in three_hour_values.keys():
            average_value = sum(three_hour_values[key]) / len(three_hour_values[key]) if three_hour_values[key] else None
            if average_value is not None:
                average_value = round(average_value, 3)  # Round to 3 decimal places
            three_hourly_averages[key].append(average_value)
        
        start_time = end_time
    
    return three_hourly_averages


def getrequest(id):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()


    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/2"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response

def day_data(data, recorded_time):
    filtered_data = {}
    interval_minutes = 2 * 60 + 30  # 2 hours and 24 minutes
    # recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in data["recorded_time"]]
    
    # Find the latest recorded time
    latest_recorded_time = recorded_time[-1]
    # print(latest_recorded_time)
    
    # Calculate the target timestamps
    target_times = [latest_recorded_time - timedelta(minutes=i*interval_minutes) for i in range(10)]
    # print(target_times)
    # print(recorded_time)
    for key, value_list in data.items():
        if key != "recorded_time":
            filtered_values = []
            for target_time in target_times:
                closest_time_index = min(range(len(recorded_time)), key=lambda i: abs(target_time - recorded_time[i]))
                # print(key)
                # print(closest_time_index)
                # index = recorded_time.index(closest_time)
                # print(index)
                # print(recorded_time[closest_time_index])
                closest_value = value_list[closest_time_index]
                # print(closest_value)
                filtered_values.append(closest_value)
            filtered_data[key] = filtered_values
    
    return filtered_data

def getdatabyhour(id):
    json_response = getrequest(id)
    recorded_time = json_response["recorded_time"]
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # Get 12-hour intervals

    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        # "flow": (0.9, 1.3)
        # Add more key-value pairs and ranges as needed
    }
    
    # Filter the data
    filtered_data = filter_data(json_response, value_ranges)
    # hourly_averages_data = calculate_3hourly_averages(filtered_data, recorded_time)
    # # hourly_averages_data = calculate_3hourly_averages(json_response, recorded_time)
    # for key, values in hourly_averages_data.items():
    #     print(f"{key}: {values}")
    # values_lists = list(hourly_averages_data.values())

    # # Create a 2D matrix
    # matrix = []
    # for values_list in values_lists:
    #     matrix.append(values_list)
    # # print(matrix)
    # return matrix
    output_data = day_data(filtered_data, recorded_time)
    matrix = [output_data[key] for key in filtered_data if key != "recorded_time"]

    # Print the matrix
    for row in matrix:
        print(row)

# if __name__ == "__main__":

#     hourly_averages_data = getdatabyhour()
#     # for key, values in hourly_averages_data.items():
#     #     print(f"{key}: {values}")


#     print(matrix)
    # Print the output
getdatabyhour("03")