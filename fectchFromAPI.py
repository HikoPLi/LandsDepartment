import json
import os


def saveData(keyword, fetchData):
    os.chdir("../LandsDepartment/data")

    with open(f"{keyword}.json", "a") as output:
        output.write(json.dumps(fetchData, sort_keys=True, indent=4))
