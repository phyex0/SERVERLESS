import requests


def print_time_and_date(url):
    """Prints the time and date"""
    response = requests.get(url)
    response_json = response.json()

    print(response_json["timezone"])
    print(response_json["utc_datetime"])
    print("GMT:" + response_json["utc_offset"])


if __name__ == '__main__':

    myTimeZone = "Europe/Istanbul"
    yourTimeZone = "Europe/Madrid"
    baseUrl = "https://worldtimeapi.org/api/timezone/"

    print_time_and_date(baseUrl + myTimeZone)
    print("************************")
    print_time_and_date(baseUrl + yourTimeZone)
