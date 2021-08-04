import requests
TIME_API_URL = "https://worldtimeapi.org/api/timezone/"


def print_time_and_date(time_zone):
    """Prints the time and date"""
    response = requests.get(TIME_API_URL + time_zone)
    response_json = response.json()

    print(response_json["timezone"])
    print(response_json["utc_datetime"])
    print("GMT:" + response_json["utc_offset"])


if __name__ == '__main__':
    """This happens when we run from the command line."""

    myTimeZone = "Europe/Istanbul"
    yourTimeZone = "Atlantic/Canary"

    print_time_and_date(myTimeZone)
    print("************************")
    print_time_and_date(yourTimeZone)
