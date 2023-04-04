import requests
# functions:
import convertXML2JSON


def download(eng=True):

    engURL = "https://www.fehd.gov.hk/english/licensing/license/text/LP_Restaurants_EN.XML"
    tchineseURL = "https://www.fehd.gov.hk/tc_chi/licensing/license/text/LP_Restaurants_TC.XML"
    # both URLs are the list of licensed restaurants in Hong Kong

    if eng == True:
        response = requests.get(engURL)
        if response.status_code == 200:
            try:
                print("Download Start !")
                data = convertXML2JSON.convert(response.content)
                with open("engXML.json", "a") as output:
                    output.write(data)
            except:
                print(f"Download Fail ! {response}")

    if eng == False:
        response = requests.get(tchineseURL)
        if response.status_code == 200:
            print("Download Start !")
            try:
                data = convertXML2JSON.convert(response.content)
                with open("TChinese.json", "a") as output:
                    output.write(data)
            except:
                print(f"Download Fail ! {response}")


download(False)
