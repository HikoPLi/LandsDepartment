import os


def open():
    os.chdir("data")
    os.system("open data.json")
    print(str(os.getcwd()))


open()
