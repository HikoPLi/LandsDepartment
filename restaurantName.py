import json
import os
import APIrequest
import fetchLocationFromJSON


def findNmaeInJSON(JSONfile):

    data = json.loads(JSONfile)
    resturantAmount = len(data["DATA"]["LPS"]["LP"])
    print(resturantAmount)
    i = 0
    while i < resturantAmount:
        for lp in data["DATA"]["LPS"]["LP"]:
            restaurantName = lp["SS"]
            restaurantName = restaurantName.replace("/", " ")
            print(restaurantName)
            APIrequest.requestAPI(restaurantName)
            fetchLocationFromJSON.location(restaurantName)

            currentDir = os.path.abspath(".")
            parentDir = os.path.dirname(currentDir)
            os.chdir(parentDir)
        i = i + 1

        return restaurantName


def name():

    with open("engXML.json") as JSONfile:

        try:
            jsonFile = JSONfile.read()
            keyword = findNmaeInJSON(jsonFile)
            return keyword

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
