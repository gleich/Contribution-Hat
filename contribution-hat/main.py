import requests
import datetime
from time import sleep
import json
import yaml
import os


def day_time_run(config):
    # Making request to get user's contributions
    url = "https://github-contributions-api.herokuapp.com/{}/count".format(
        config["username"])
    response = requests.request("GET", url).json()

    # Getting max number of contributions for the current year
    max_contributions = 0
    for i in range(365):
        date = datetime.date.today() - datetime.timedelta(i)
        contributions = response["data"][str(
            date.year)][str(date.month)][str(date.day)]
        if contributions > max_contributions:
            max_contributions = contributions

    # Setting LEDs
    values = []
    for i in reversed(range(64)):
        date = datetime.date.today() - datetime.timedelta(i)
        contributions = response["data"][str(
            date.year)][str(date.month)][str(date.day)]
        if contributions != 0:
            percentage_of_max = contributions / max_contributions
        else:
            percentage_of_max = 0
        print("{}/{}/{}".format(date.month, date.day, date.year))
        print("\tPercentage of max", percentage_of_max)
        print("\tIndex", i)
        print("\t Contributions", contributions)
        if percentage_of_max == 0:
            values.append([255, 0, 0])
        elif percentage_of_max < 0.25:
            values.append([255, 154, 2])
        elif percentage_of_max < 0.50:
            values.append([252, 248, 0])
        elif percentage_of_max < 0.75:
            values.append([0, 255, 0])
        else:
            values.append([25, 73, 13])
    with open("./sense_hat_containerized/leds.json", "w") as leds_json:
        json.dump(values, leds_json)
    sleep(30)


while True:
    # Loading from yaml file
    with open("./contribution-hat-config/config.yaml") as config_file:
        config = yaml.load(config_file)
    os.environ["TZ"] = config["timezone"]
    if "off-hours" in config.keys():
        if datetime.datetime.now().hour in config["off-hours"]:
            clear_vals = []
            for i in range(64):
                clear_vals.append([0, 0, 0])
            with open("./sense_hat_containerized/leds.json", "w") as leds_json:
                json.dump(clear_vals, leds_json)
            sleep(30)
        else:
            day_time_run(config)
    else:
        day_time_run(config)
