import requests

requestHeader = {
    "Content-Type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Connection": "close"
}


def convert(east, north):
    api = f"http://www.geodetic.gov.hk/transform/v2/?inSys=hkgrid&e={east}&n={north}"
    response = requests.get(api, headers=requestHeader)
    fetchData = response.json()
    print(fetchData)
    return fetchData
