import csv
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


def subtract_data(first_data, second_data):
    # Find the common recorded times
    common_times = set(first_data["recorded_time"]) & set(second_data["recorded_time"])

    # Remove common data from the first data
    for key in first_data:
        if key != "recorded_time":
            first_data[key] = [value for time, value in zip(first_data["recorded_time"], first_data[key]) if time not in common_times]
    
    return first_data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow(["recorded_time"] + list(data.keys()))
        
        # Write the data rows
        for values in zip(data["recorded_time"], *data.values()):
            writer.writerow(values)
def getrequest(days):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()


    get_url = f"https://api.thingzcloud.com/devices/getData/AQM00003/{days}"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response


def savedataincsv(date_one_str, date_two_str):
    # Convert the date strings to datetime objects
    date_one = datetime.strptime(date_one_str, "%Y-%m-%d")
    date_two = datetime.strptime(date_two_str, "%Y-%m-%d")

    # Calculate the number of days passed till today for both dates
    today = datetime.now()
    days_passed_date_one = (today - date_one).days
    days_passed_date_two = (today - date_two).days 
    print(days_passed_date_one)
    print(days_passed_date_two)
    
    json_response = getrequest(days_passed_date_one)
    json_response1 = getrequest(days_passed_date_two)
    # Define the ranges for filtering
    value_ranges = {
        "temperature": (0, 50),
        "humidity": (0, 100),
        "flow": (0.9, 1.1)
        # Add more key-value pairs and ranges as needed
    }
    
    # Filter the data
    filtered_data = filter_data(json_response, value_ranges)
    filtered_data1 = filter_data(json_response1, value_ranges)

    # Subtract the common data from the first data
    subtracted_data = subtract_data(filtered_data, filtered_data1)
    
    # Save the subtracted data to CSV
    save_to_csv(subtracted_data, "subtracted_data.csv")

# savedataincsv("2023-08-12", "2023-08-16")



# if __name__ == "__main__":
#    # Dates in python format (replace these with your actual dates)
#     date_one_str = "2023-08-10"  # Replace with the first date in "YYYY-MM-DD" format
#     date_two_str = "2023-08-14"  # Replace with the second date in "YYYY-MM-DD" format

#     # Convert the date strings to datetime objects
#     date_one = datetime.strptime(date_one_str, "%Y-%m-%d")
#     date_two = datetime.strptime(date_two_str, "%Y-%m-%d")

#     # Calculate the number of days passed till today for both dates
#     today = datetime.now()
#     days_passed_date_one = (today - date_one).days
#     days_passed_date_two = (today - date_two).days 
#     print(days_passed_date_one)
#     print(days_passed_date_two)
    
#     json_response = getrequest(days_passed_date_one)
#     json_response1 = getrequest(days_passed_date_two)
#     # Define the ranges for filtering
#     value_ranges = {
#         "temperature": (0, 50),
#         "humidity": (0, 100),
#         "flow": (0.9, 1.1)
#         # Add more key-value pairs and ranges as needed
#     }
    
#     # Filter the data
#     filtered_data = filter_data(json_response, value_ranges)
#     filtered_data1 = filter_data(json_response1, value_ranges)

#     # Subtract the common data from the first data
#     subtracted_data = subtract_data(filtered_data, filtered_data1)
    
#     # Save the subtracted data to CSV
#     save_to_csv(subtracted_data, "subtracted_data.csv")
