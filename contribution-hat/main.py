import requests
import yaml
from datetime import date, timedelta, datetime
from sense_hat import SenseHat
from time import sleep
import json

# Loading from yaml file
with open("./contribution-hat-config/username.txt") as username_file:
    username = username_file.read()

sense = SenseHat()
sense.clear()

while True:
    if datetime.now().hour < 6 and datetime.now().hour > 22:
        sense.clear()
        sleep(10)
    else:
        # Making request to get user's contributions
        url = "https://github-contributions-api.herokuapp.com/{}/count".format(
            username)
        response = requests.request("GET", url).json()

        # Getting max number of contributions for the current year
        max_contributions = 0
        for i in range(365):
            date = date.today() - timedelta(i)
            contributions = response["data"][date.year][date.month][date.day]
            if contributions > max_contributions:
                max_contributions = contributions

        # Setting LEDs
        values = []
        for i in reversed(range(64)):
            date = date.today() - timedelta(i)
            contributions = response["data"][date.year][date.month][date.day]
            percentage_of_max = max_contributions / contributions
            if percentage_of_max == 0:
                values.append([250, 250, 250])
            elif percentage_of_max < 25:
                values.append([198, 228, 139])
            elif percentage_of_max < 50:
                values.append([123, 201, 111])
            elif percentage_of_max < 75:
                values.append([35, 154, 59])
            else:
                values.append([25, 97, 39])
        with open("./sense_hat_containerized/leds.json", "w") as leds_json:
            json.dump(values, leds_json)
        sleep(10)
