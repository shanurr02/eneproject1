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


def fetch_data(id):
    with open("token.txt", "r") as f:
        tk = f.read().strip()

    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/2"
    header = {"x-api-key": tk}
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response

def extract_day_data(data, recorded_time):
    interval_minutes = 2 * 60 + 30  # 2 hours and 30 minutes
    latest_recorded_time = recorded_time[-1]
    target_times = [latest_recorded_time - timedelta(minutes=i * interval_minutes) for i in range(11)]
    print(target_times)
    print(len(recorded_time))
    filtered_data = {}
    for key, value_list in data.items():
        if key != "recorded_time":
            filtered_values = []
            print(len(value_list))
            for target_time in target_times:
                closest_time_index = min(range(len(recorded_time)), key=lambda i: abs(target_time - recorded_time[i]))
                print(closest_time_index)
                closest_value = value_list[closest_time_index%(len(recorded_time)-5)]
                filtered_values.append(closest_value)
            filtered_data[key] = filtered_values
    
    return filtered_data

def get_data_by_hour(id):
    json_response = fetch_data(id)
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in json_response["recorded_time"]]

    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
         # "flow": (0.9, 1.3)
        # Add more key-value pairs and ranges as needed
    }
    
    filtered_data = filter_data(json_response, value_ranges)
    output_data = extract_day_data(filtered_data, recorded_time)
    matrix = [output_data[key] for key in filtered_data if key != "recorded_time"]
    # print(matrix)
    return matrix

if __name__ == "__main__":
    hourly_averages_data = get_data_by_hour("03")
    for i, row in enumerate(hourly_averages_data, start=1):
        print(f"Row {i}: {row}")