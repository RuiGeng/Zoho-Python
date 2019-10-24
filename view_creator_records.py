import urllib.parse
import urllib.request
import json
import csv
import os

# URL Format
# https://creator.zoho.com/api/<format>/<applicationLinkName>/view/<viewLinkName>


url = "https://creator.zoho.com/api/json/polaron-reference-data/view/Deal_and_Projects_Report"
authtoken = "411ec6b991ed77bb876b2c78dc2659e5"
scope = "creatorapi"
zc_ownername = "polaronsolartech"
raw = "true"

params = {"authtoken": authtoken, "scope": scope, "zc_ownername": zc_ownername, "raw": raw}
query_string = urllib.parse.urlencode(params)
reqUrl = url + "?" + query_string

try:
    with urllib.request.urlopen(reqUrl) as response:
        content = response.read().decode('utf-8')
        data = json.loads(content)
        for d in data['Deal_and_Projects']:
            print(d.get('Accounting_Identity'))
except urllib.error.HTTPError as error:
    print("Error Code: " + str(error.code))
