import requests
first_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
from datetime import datetime
now = datetime.now()
day = now.strftime("%y/%m/%d")

time = now.strftime("%H:%M")

first_param = {
 "query": input("what did you do as an excercise?  "),
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}
first_header = {
    "x-app-id":"",
    "x-app-key": ""


}

first_response = requests.post(url=first_endpoint, json=first_param, headers = first_header)

data = first_response.json()["exercises"][0]
print(data)










endpoint = "https://api.sheety.co/simane9876/WorkoutTracking/workouts"
next_endpoint = "https://api.sheety.co/b331d7cee5d6b3e332cc8926a4f6026a/workoutTracking/workouts"

param = {
    "workout": {
        "date": day,
        "time": time,
        "exercise": data['name'],
        "duration": f"{data['duration_min']} min",
        "calories": f"{data['nf_calories']} Kcal"
    }
}

header = {"Authorization": ""}

response = requests.post(url=next_endpoint, json=param, headers=header)

print(response.text)
