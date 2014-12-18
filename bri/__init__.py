import csv
from bson import ObjectId
from pymongo import MongoClient
from slugify import slugify
from bson import json_util

mongo = MongoClient()
businesses = mongo.br.businesses

# Clear collections before running importer
#businesses.remove({})


def import_data(json_filepath):

    with open (json_filepath, "r") as jsonfile:
        json_str = jsonfile.read()
        json_biz_array = json_util.loads(json_str)

        for json_biz in json_biz_array:

            json_biz['business_type'] = ""

            json_biz['picture'] = {
                "inside": "",
                "outside": "",
                "panorama": "",
            }

            json_biz['business_name'] = json_biz['company_name']
            json_biz.pop("company_name", None)

            businesses.save(json_biz)
