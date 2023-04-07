import requests
import json
import os
# functions

requestHeader = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Connection": "close"
}


def saveData(keyword, fetchData):
    # save data fectched from API to file
    data = json.dumps(fetchData, ensure_ascii=False, sort_keys=True, indent=4)

    os.chdir("../LandsDepartment/data")
    with open(f"{keyword}.json", "a") as output:
        output.write(data)


def requestAPI(keyword):

    apiURL = f"https://www.map.gov.hk/gih-ws2/search?keyword={keyword}#0"
    response = requests.get(apiURL, headers=requestHeader)
    fetchData = response.json()
    # save fetchData
    saveData(keyword, fetchData)
