import requests

TIME_API_URL = "https://worldtimeapi.org/api/timezone/"
WEATHER_API_URL = "https://weather.com/weather/today/l/"


def print_time_and_date(time_zone):
    """Prints the time and date"""
    response = requests.get(TIME_API_URL + time_zone)
    response_json = response.json()

    print(response_json["timezone"])
    print(response_json["utc_datetime"])
    print("GMT:" + response_json["utc_offset"])


def get_weather(city_name):
    """Prints weather"""
    geo_code = get_geo_code(city_name)
    weather_api_end = "?par=google"
    response = requests.get(WEATHER_API_URL + geo_code + weather_api_end)

    get_temp(str(response.content), city_name)


def get_temp(weather_html, city_name):
    """Finding the temperature value from the html file and print."""
    searched_part = '<span data-testid="TemperatureValue" class="CurrentConditions--tempValue--3a50n">'
    index = weather_html.find(searched_part) + len(
        searched_part
    )  # gives you beginning index

    temp = weather_html[index] + weather_html[index + 1]
    print("Temp of the " + city_name + " is : " + temp + "F")
    print("Temp of the " + city_name + " is : " + fahrenheit_to_celsius(temp) + "C")


def fahrenheit_to_celsius(temp):
    """Converting temperature values Fahrenheit to Celsius."""
    return str(round((int(temp) - 32) * 5 / 9))


def get_payload(city_name):
    """returns payload"""
    payload = (
        "&address="
        + city_name_checker(city_name)
        + "&region=UK&lcode=rYz26de5Gs7Ey134&lid=14632879&code=st0PlEa3"
    )

    return payload


def get_geo_code(city_name):
    """Get the geocode by the city name. First reformat the city name then return goecode."""
    url = "https://www.mapdevelopers.com/data.php?operation=geocode"
    payload = get_payload(city_name)
    headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
    response = requests.request("POST", url, headers=headers, data=payload)

    while True:
        if len(response.json()["data"]) == 0:
            print("You've entered invalid city. Please enter again !")
            response = requests.request(
                "POST", url, headers=headers, data=get_payload(input())
            )
        else:
            break

    response_geocode = (
        str(response.json()["data"]["lat"]) + "," + str(response.json()["data"]["lng"])
    )

    return response_geocode


def city_name_checker(city_name):
    """If the length of the city name is greater than one the format of the city name must be like that : Los%20Angles ."""
    valid_name = ""
    names = city_name.split(" ")

    for i in range(len(names)):
        names[i] = names[i].capitalize()

    valid_name += names[0]

    if len(names) > 1:
        for i in range(1, len(names)):
            valid_name += "%20" + names[i]

    return valid_name


if __name__ == "__main__":

    my_time_zone = "Europe/Istanbul"
    your_time_zone = "Atlantic/Canary"

    print_time_and_date(my_time_zone)
    print("***********************")
    print_time_and_date(your_time_zone)
    print("***********************")
    get_weather(input("Enter a city name : "))
