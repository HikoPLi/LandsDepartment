import xmltodict
import json


def convert(XMLdata):

    orderedDirct = xmltodict.parse(XMLdata)
    jsonData = json.dumps(orderedDirct, sort_keys=True, indent=4)

    return jsonData
