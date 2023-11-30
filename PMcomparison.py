from datetime import datetime, timedelta
import requests
import matplotlib.pyplot as plt
import numpy as np
from tempvsrhvspm import get_24_hour_intervals
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

    for time, temp, hum,flow, pm1, pm2_5, pm10, tsp, pq0_3, pq0_5, pq1_0, pq2_5, pq5_0, pq10 in zip(recorded_time, data["temperature"], data["humidity"],data['flow'], data["PM1_0"], data["PM2_5"], data["PM10"], data["TSP"], data['PQ0_3'],data['PQ0_5'],data['PQ1_0'],data['PQ2_5'],data['PQ5_0'],data['PQ10'],):
        if time <= midpoint:
            week1_data["temperature"].append(temp)
            week1_data["humidity"].append(hum)
            week1_data["flow"].append(flow)
            week1_data["PM1_0"].append(pm1)
            week1_data["PM2_5"].append(pm2_5)
            week1_data["PM10"].append(pm10)
            week1_data["TSP"].append(tsp)
            week1_data["PQ0_3"].append(pq0_3)
            week1_data["PQ0_5"].append(pq0_5)
            week1_data["PQ1_0"].append(pq1_0)
            week1_data["PQ2_5"].append(pq2_5)
            week1_data["PQ5_0"].append(pq0_5)
            week1_data["PQ10"].append(pq10)
        else:
            week2_data["temperature"].append(temp)
            week2_data["humidity"].append(hum)
            week2_data["flow"].append(flow)
            week2_data["PM1_0"].append(pm1)
            week2_data["PM2_5"].append(pm2_5)
            week2_data["PM10"].append(pm10)
            week2_data["TSP"].append(tsp)
            week2_data["PQ0_3"].append(pq0_3)
            week2_data["PQ0_5"].append(pq0_5)
            week2_data["PQ1_0"].append(pq1_0)
            week2_data["PQ2_5"].append(pq2_5)
            week2_data["PQ5_0"].append(pq0_5)
            week2_data["PQ10"].append(pq10)


    return week1_data, week2_data

def calculate_averages(data):
    averages = {}
    for key, values in data.items():
        averages[key] = round(sum(values) / len(values), 3) if values else None
    return averages

def getrequest(id, days):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()

    print(days)
    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/{days}"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response
    
def plot_dual_line_graph(data1, data2, start_day, title):
    # Ensure both data lists have exactly 14 points
    # if len(data1) != 14 or len(data2) != 14:
    #     raise ValueError("Both data lists should contain exactly 14 points.")

    # Define the order of days in a week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Reorder the days to start from the specified start_day
    start_index = days_of_week.index(start_day)
    ordered_days = days_of_week[start_index:] + days_of_week[:start_index]

    # Create labels for each data point based on day and time
    labels = []
    for day in ordered_days:
        labels.extend([f"{day} - Day", f"{day} - Night"])

    # Plotting
    x = np.arange(len(labels))

    plt.plot(x, data1, marker='o', label='Last week')
    plt.plot(x, data2, marker='o', label='Current week')

    plt.xticks(x, labels, rotation=30, ha="right")
    plt.xlabel("Day of the Week and Time of Day")
    plt.ylabel("Data Points")
    plt.title(f"Line Graph of {title} Data Points for Each Day and Time of Day")
    plt.legend()
    plt.show()


def getdatabyweek(id , days):
    json_response = getrequest(id, days)
    recorded_time = json_response["recorded_time"]
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        "flow": (0.9, 1.1),
        "PM1_0": (0,400)
        # Add more key-value pairs and ranges as needed
    }
    
    # Filter the data
    week1 , week2 = split_data_by_weeks(recorded_time, json_response)
    filtered_data1 = filter_data(week1, value_ranges)
    filtered_data2 = filter_data(week2, value_ranges)
    # Get 12-hour intervals
    # data_intervals = get_24_hour_intervals(json_response, recorded_time)
    data_intervals_week1 = get_24_hour_intervals(filtered_data1, recorded_time)
    data_intervals_week2 = get_24_hour_intervals(filtered_data2, recorded_time)
    
    # # Rearrange the output to the desired format
    output_format_week1 = {key: [interval_data[key] for interval_data in data_intervals_week1] for key in data_intervals_week1[0]}
    output_format_week2 = {key: [interval_data[key] for interval_data in data_intervals_week2] for key in data_intervals_week2[0]}
    values_lists_week1 = list(output_format_week1.values())
    for key, average_values in output_format_week1.items():
        print(f"{key}: {average_values}")
    values_lists_week2 = list(output_format_week2.values())
    for key, average_values in output_format_week2.items():
        print(f"{key}: {average_values}")
    # Create a 2D matrix
    matrix_week1 = []
    matrix_week2 = []
    for values_list in values_lists_week1:
        matrix_week1.append(values_list)
    for values_list in values_lists_week2:
        matrix_week2.append(values_list)

    # print(matrix_week1)
    # print(matrix_week2)
    # print(recorded_time[0])
    date_object = datetime.strptime(f"{recorded_time[0]}", "%Y-%m-%d %H:%M:%S")
    day_of_week = find_day(date_object)
    return matrix_week1, matrix_week2, day_of_week


def find_day(date):
    # Assuming 'date' is a datetime object
    day_string = date.strftime("%A")
    return day_string

# getdatabyweek("03")

def main():
    matrix_week1, matrix_week2, weekstart = getdatabyweek("03" , "14")
    # temperature = matrix[0]
    # humidity = matrix[1]
    tempw1 = matrix_week1[0]
    tempw2 = matrix_week2[0]
    humidityw1 = matrix_week1[1]
    humidityw2 = matrix_week2[1]

    pm1_w1 = matrix_week1[4]
    pm2_5_w1 = matrix_week1[5]
    pm10_w1 = matrix_week1[6]
    tsp_w1 = matrix_week1[3]
    pm1_w2 = matrix_week2[4]
    pm2_5_w2 = matrix_week2[5]
    pm10_w2 = matrix_week2[6]
    tsp_w2 = matrix_week2[3]
    # # Plotting
    plot_dual_line_graph(tempw1,tempw2, weekstart, "Temperature")
    plot_dual_line_graph(humidityw1,humidityw2, weekstart, "Humidity")
    plot_dual_line_graph(pm1_w1,pm1_w2, weekstart, "PM1")
    plot_dual_line_graph(pm2_5_w1,pm2_5_w2, weekstart, "PM2_5")
    plot_dual_line_graph(pm10_w1,pm10_w2, weekstart, "PM10")
    plot_dual_line_graph(tsp_w1,tsp_w2, weekstart, "TSP")

if __name__ == "__main__":
    main()