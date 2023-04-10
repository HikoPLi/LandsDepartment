import restaurantName
import time
import math
import os

# import downloadXMLfromWeb


def parentPath():
    currentDir = os.path.abspath(".")
    parentDir = os.path.dirname(currentDir)
    os.chdir(parentDir)


def main():

    os.chdir("../LandsDepartment/data")
    with open("data.json", "w") as rewriteFile:
        rewriteFile.write("")

    parentPath()

    # downloadXMLfromWeb.download(True) # True for Rng, False for Chinese
    restaurantName.name()


if "_name_" == "_name_":
    startTime = time.time()
    main()
    endTime = time.time()

    print("used time is {} s".format(math.ceil(endTime - startTime)))

    os.system("cd data/")
    os.system("open data.json")
