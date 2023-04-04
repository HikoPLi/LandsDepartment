import APIrequest
import fetchLocationFromJSON


def main():
    keyword = "東方之珠"
    APIrequest.requestAPI(keyword)
    fetchLocationFromJSON.location(keyword)


main()
