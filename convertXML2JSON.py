import xmltodict
import json


def convert(XMLdata):

    orderedDirct = xmltodict.parse(XMLdata, force_cdata=True)
    jsonData = json.dumps(orderedDirct, ensure_ascii=False,
                          sort_keys=True, indent=4)

    return jsonData
