import requests
import fectchFromAPI

requestHeader = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Connection": "close"
}


def requestAPI(keyword):

    apiURL = f"https://www.map.gov.hk/gih-ws2/search?keyword={keyword}#0"
    response = requests.get(apiURL, headers=requestHeader)
    fetchData = str(response.json())
    print(fetchData)
    fectchFromAPI.saveData(keyword, fetchData)
