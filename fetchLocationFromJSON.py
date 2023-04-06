import json
from re import findall


def findAll(jsonFile):
    jsonObject = json.load(jsonFile)
    resultAmount = len(jsonObject)

    i = 0
    while i < resultAmount:

        english_name = jsonObject[i]['ename']
        chinese_name = jsonObject[i]['cname']
        east = jsonObject[i]['easting']
        north = jsonObject[i]['northing']
        string_address = f"{east},{north}"
        i = i + 1

        print(string_address, english_name, chinese_name)

        if i == resultAmount:
            break

    # return east, north


def location(keyword):
    # access path: "..../LandsDepartment/data"
    with open(f"{keyword}.json") as JSONfile:

        try:
            findAll(JSONfile)

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
