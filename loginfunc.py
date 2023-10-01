import requests

def loginrequest(username , password) :
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

        # Extract the token from the response JSON
        tk = json_data.get("token", "")
        # Save the token to a file
        with open("token.txt", "w") as f:
            f.write(tk)
        return True
    else:
        print("Login failed. Status code:", response.status_code)
        return False


loginrequest("shanurrahman02@gmail.com", "rahman@02")