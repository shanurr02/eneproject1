import requests
from status import check_last_recorded_time_within_10_minute
def devicedetails(username , password) :
    # API endpoint and login credentials
    api_url = "https://api.thingzcloud.com/users/login"

    # Prepare the request payload
    payload = {
        "email": username,
        "password": password
    }

    # Send the POST request
    response = requests.post(api_url, json=payload)
    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()
        print("Login sucessful")
        tk = json_data.get("token", "")
        # Save the token to a file
        with open("token.txt", "w") as f:
            f.write(tk)
        # Extract the required information
        name = json_data["userDetails"]["name"]
        no_of_devices = len(json_data["devices"])
        device_ids = [device["deviceDetails"]["device_id"] for device in json_data["devices"]]

        # Create the output dictionary
        output_dict = {
            "Name": name,
            "Number_of_Devices": no_of_devices,
            "Device_IDs": device_ids
        }
        active_device_ids = []
        for id in device_ids:
            if check_last_recorded_time_within_10_minute(id):
                active_device_ids.append(id)
        output_dict["Active_devices"] = active_device_ids
        # output_dict.update(["Active_devices", active_device_ids])
        print(output_dict)
        return True
    else:
        print("Login failed. Status code:", response.status_code)
        return False


devicedetails("shanurrahman02@gmail.com", "rahman@02")