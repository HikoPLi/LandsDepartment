import json
from re import findall


def findAll(jsonFile):
    jsonObject = json.loads(str(jsonFile))
    english_name = jsonObject['ename']
    chinese_name = jsonObject['cname']
    east = jsonObject['easting']
    north = jsonObject['northing']
    string_address = f"{east},{north}"

    return string_address, english_name, chinese_name


def location(keyword):
    # access path: "..../LandsDepartment/data"
    with open(f"{keyword}.json") as JSONfile:

        try:
            print(findAll(json.load(JSONfile)))

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
