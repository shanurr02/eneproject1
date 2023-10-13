import requests
from datetime import datetime, timedelta


def getrequest(id):
    # Read the token from the file
    with open("token.txt", "r") as f:
        tk = f.read().strip()

    dd = datetime.now().date()
    print(dd) 
    get_url = f"https://api.thingzcloud.com/devices/getDataByDate/AQM000{id}/{dd}/{dd}/d"  
    # get_url = f"https://api.thingzcloud.com/devices/getData/{id}/1"
    header = {
        "x-api-key": tk
    }
    get_response = requests.get(get_url, headers=header)
    json_response = get_response.json()

    return json_response

def check_last_recorded_time_within_10_minute(id):
    try:
        json_response = getrequest(id)
        recorded_time = json_response.get("recorded_time")
        if recorded_time:
            last_recorded_time_str = recorded_time[-1]
            last_recorded_time = datetime.strptime(last_recorded_time_str, "%m/%d/%Y, %H:%M:%S")
            current_time = datetime.now()
            
            time_difference = current_time - last_recorded_time
            if time_difference <= timedelta(minutes=8):
                return True
            else:
                return False
        else:
            return False
        
    except Exception as e:
        print("Error:", e)
        return False
# print(check_last_recorded_time_within_1_minute())
# if __name__ == "__main__":
#     print(check_last_recorded_time_within_1_minute())
    # Read the token from the file
    # with open("token.txt", "r") as f:
    #     tk = f.read().strip()

    # api_url = "https://api.thingzcloud.com/devices/getData/AQM00003/1"
    # headers = {
    #     "x-api-key": tk
    # }

    # response = requests.get(api_url, headers=headers)
    # json_response = response.json()

    # result = check_last_recorded_time_within_1_minute(json_response)
    # print("Last recorded time within 1 minute:", result)

if __name__ == "__main__":
    print(check_last_recorded_time_within_10_minute("03"))
