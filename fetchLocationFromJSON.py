import json
import time
import signal

from re import findall
# Function
import convertWGS84ToEPSG2326


class TimeoutError(Exception):
    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def time_out(interval, callback):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError(
                "run func timeout (for one process). Out of 20 Sec.")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)
                result = func(*args, **kwargs)
                signal.alarm(0)
                return result
            except TimeoutError as e:
                callback(e)
        return wrapper
    return decorator


def timeout_callback(e):
    print(e.msg)

# ⬆⬆ Function for timeout. Reference from csdn
# https://blog.csdn.net/weixin_42368421/article/details/101354628


@time_out(20, timeout_callback)
def findAll(jsonFile):
    jsonObject = json.load(jsonFile)
    resultAmount = len(jsonObject)

    i = 0
    while i < resultAmount:

        if jsonObject[i]['ename'] != "":
            if jsonObject[i]['cname'] != "":
                englishName = jsonObject[i]['ename']
                chineseName = jsonObject[i]['cname']
                east = jsonObject[i]['easting']
                north = jsonObject[i]['northing']
                string_address = f"east:{east}, north:{north}"

                i = i + 1

                print(string_address, englishName, chineseName)

                EPSG2326 = convertWGS84ToEPSG2326.convert(east, north)

                with open(f"data.json", "a") as output:
                    output.write("\n")
                    output.write(
                        f"{EPSG2326}, {englishName}, {chineseName}")

        if i == resultAmount:
            break


def convert_address_to_WGS84(keyword):
    # access path: "..../LandsDepartment/data"
    with open(f"{keyword}.json") as JSONfile:

        try:
            findAll(JSONfile)

        except json.JSONDecodeError as e:

            print(f"Invalid JSON: {e}")
