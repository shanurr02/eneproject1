import requests
# Read the token from the file
with open("token.txt", "r") as f:
    tk = f.read().strip()



# Set the headers with the token
header = {
    "x-api-key": tk
}
latest_data = []

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

def get_data(id):   
    get_url = f"https://api.thingzcloud.com/devices/getData/AQM000{id}/1"
    latest_data = []
    get_response = requests.get(get_url, headers=header)
    
    # Check if the GET request was successful
    if get_response.status_code == 200:
        # Process the response
        json_response = get_response.json()

        # Iterate over each key in the response JSON
        for key, value_list in json_response.items():
            if key == "error":
                print(json_response)
                print("Error logging! Login Again")
                continue

            # Check if the value is a list
            if isinstance(value_list, list) and len(value_list) > 0:
                # Iterate through the value list in reverse order
                latest_value = None
                for value in reversed(value_list):
                    if value is not None and value != "null" and value != 0:
                        latest_value = value
                        break  # Stop iterating once the latest non-zero, non-None value is found
                latest_data.append(latest_value)

                print(f"Key: {key}, Latest Value: {latest_value}")
            else:
                print(f"Key: {key}, Value is not a list or empty")
    else:
        print("GET request failed. Status code:", get_response.status_code)
    # print(latest_data)
    return latest_data


# get_data()