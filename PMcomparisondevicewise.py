from datetime import datetime,timedelta
from PMcomparison import filter_data, find_day, getrequest
from tempvsrhvspm import get_24_hour_intervals
import matplotlib.pyplot as plt
import numpy as np
import requests

def fetch_data(id):
    with open("token.txt", "r") as f:
        tk = f.read().strip()
    dd = datetime.now().date()
    # print(dd)
    dd1 = dd + timedelta(days=-6)
    # print(dd1)
    get_url = f"https://api.thingzcloud.com/devices/getDataByDate/AQM000{id}/{dd1}/{dd}/d"
    # get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/2"
    header = {"x-api-key": tk}
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response
def getdatabyweek(id1, id2 , days):
    # print(days)
    json_response1 = getrequest(id2, days)
    print("D1")
    json_response2 = fetch_data(id1)
    print("D2")
    recorded_time = json_response1["recorded_time"]
    recorded_time = [datetime.strptime(time_str, "%m/%d/%Y, %H:%M:%S") for time_str in recorded_time]
    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        "flow": (0.9, 1.1)
        # Add more key-value pairs and ranges as needed
    }
    
    # Filter the data
    filtered_data1 = filter_data(json_response1, value_ranges)
    filtered_data2 = filter_data(json_response2, value_ranges)
    # Get 12-hour intervals
    # data_intervals = get_24_hour_intervals(json_response, recorded_time)
    data_intervals_week1 = get_24_hour_intervals(filtered_data1, recorded_time)
    print("AQM00003 done")
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

    plt.plot(x, data1, marker='o', label='AQM00002')
    plt.plot(x, data2, marker='o', label='AQM00003')

    plt.xticks(x, labels, rotation=30, ha="right")
    plt.xlabel("Day of the Week and Time of Day")
    plt.ylabel("Data Points")
    plt.title(f"Line Graph of {title} Data Points for Each Day and Time of Day")
    plt.legend()
    plt.show()

def main():
    matrix_week1, matrix_week2, weekstart = getdatabyweek("02", "03", "07")
    # temperature = matrix[0]
    # humidity = matrix[1]
    pm1_w1 = matrix_week1[4]
    pm2_5_w1 = matrix_week1[5]
    pm10_w1 = matrix_week1[6]
    tsp_w1 = matrix_week1[3]
    pm1_w2 = matrix_week2[4]
    pm2_5_w2 = matrix_week2[5]
    pm10_w2 = matrix_week2[6]
    tsp_w2 = matrix_week2[3]
    # # Plotting
    plot_dual_line_graph(pm1_w1,pm1_w2, weekstart, "PM1")
    plot_dual_line_graph(pm2_5_w1,pm2_5_w2, weekstart, "PM2_5")
    plot_dual_line_graph(pm10_w1,pm10_w2, weekstart, "PM10")
    plot_dual_line_graph(tsp_w1,tsp_w2, weekstart, "TSP")

if __name__ == "__main__":
    main()