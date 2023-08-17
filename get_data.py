import requests
# Read the token from the file
with open("token.txt", "r") as f:
    tk = f.read().strip()


get_url = "https://api.thingzcloud.com/devices/getData/AQM00003/1"

# Set the headers with the token
header = {
    "x-api-key": tk
}
latest_data = []


def get_data():
    latest_data = []
    get_response = requests.get(get_url, headers=header)
    # Check if the GET request was successful
    if get_response.status_code == 200:
        # Process the response
        json_response = get_response.json()
        # print(json_response.get("recorded_time", ""))

        # Iterate over each key in the response JSON
        for key, value_list in json_response.items():
            if key == "error":
                print(json_response)
                print("Error loging! Login Again")
            # Check if the value is a list
            if isinstance(value_list, list) and len(value_list) > 0:
                # Get the last value from the list
                last_value = value_list[-1]
                latest_data.append(last_value)
                
                print(f"Key: {key}, Last Value: {last_value}")
            else:
                print(f"Key: {key}, Value is not a list or empty")
    else:
        print("GET request failed. Status code:", get_response.status_code)

    return latest_data

get_data()