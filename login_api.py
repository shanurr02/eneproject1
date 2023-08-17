from json.tool import main
import requests

# API endpoint and login credentials
api_url = "https://api.thingzcloud.com/users/login"
username = "shanurrahman02@gmail.com"
password = "rahman@02"

# Prepare the request payload
payload = {
    "email": username,
    "password": password
}


def loginrequest() :
    # Send the POST request
    response = requests.post(api_url, json=payload)

    if response.status_code == 200:
        # Parse the JSON response
        json_data = response.json()

        # Extract the token from the response JSON
        tk = json_data.get("token", "")
        # Save the token to a file
        with open("token.txt", "w") as f:
            f.write(tk)

    else:
        print("Login failed. Status code:", response.status_code)


loginrequest()