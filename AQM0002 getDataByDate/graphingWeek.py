from datetime import datetime, timedelta
import requests


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

    dd = datetime.now().date() + timedelta(days=-7)
    dd1 = dd + timedelta(days=-8)
    print(dd1)
    get_url = f"https://api.thingzcloud.com/devices/getDataByDate/AQM000{id}/{dd}/{dd1}/d"
    print(get_url)
    # get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/7"
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

getdatabyweek("02")
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
