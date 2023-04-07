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
            if lp["DIST"] == "17":  # "17" is district code
                restaurantName = lp["SS"]
                restaurantName = restaurantName.replace("/", " ")
                restaurantName = restaurantName.replace("%", " ")
                restaurantName = restaurantName.replace("!", " ")
                restaurantName = restaurantName.replace(")", " ")
                restaurantName = restaurantName.replace("(", " ")
                print(restaurantName)
                APIrequest.requestAPI(restaurantName)
                fetchLocationFromJSON.convert_address_to_WGS84(restaurantName)

                currentDir = os.path.abspath(".")
                parentDir = os.path.dirname(currentDir)
                os.chdir(parentDir)
        i = i + 1

        if i == resturantAmount:
            break

        return restaurantName


def name():

    with open("engXML.json") as JSONfile:

        try:
            jsonFile = JSONfile.read()
            keyword = findNmaeInJSON(jsonFile)
            return keyword

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
