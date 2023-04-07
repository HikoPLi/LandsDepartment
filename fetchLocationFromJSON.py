import json
from re import findall
# Function
import convertWGS84ToEPSG22326


def findAll(jsonFile):
    jsonObject = json.load(jsonFile)
    resultAmount = len(jsonObject)

    i = 0
    while i < resultAmount:

        englishName = jsonObject[i]['ename']
        chineseName = jsonObject[i]['cname']
        east = jsonObject[i]['easting']
        north = jsonObject[i]['northing']
        string_address = f"east:{east}, north:{north}"

        i = i + 1

        print(string_address, englishName, chineseName)

        with open(f"data.csv", "a") as output:
            output.write("\n")
            output.write(f"{string_address}, {englishName}, {chineseName}")

        if i == resultAmount:
            break

    # convertWGS84ToEPSG22326.convert(string_address)


def convert_address_to_WGS84(keyword):
    # access path: "..../LandsDepartment/data"
    with open(f"{keyword}.json") as JSONfile:

        try:
            findAll(JSONfile)

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
