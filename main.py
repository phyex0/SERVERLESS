import json, requests

def printTimeDate(url):

    response = requests.get(url)
    responseJSON = response.json()

    print(responseJSON["timezone"])
    print(responseJSON["utc_datetime"])
    print("GMT:"+ responseJSON["utc_offset"])



if __name__ == '__main__':

    myTimeZone ="Europe/Istanbul"
    yourTimeZone = "Europe/Madrid"
    baseUrl = "http://worldtimeapi.org/api/timezone/"

    printTimeDate(baseUrl+myTimeZone)
    print("************************")
    printTimeDate(baseUrl+yourTimeZone)




