import urllib.parse
import urllib.request
import json
import csv
import os

# Remove file
if os.path.exists('Records.csv'):
    os.remove('Records.csv')

# URL Format
# https://creator.zoho.com/api/<format>/<applicationLinkName>/view/<viewLinkName>

url = "https://creator.zoho.com/api/csv/accounting-space/view/CRM_Info_Report"
authtoken = "abcdefg"
scope = "creatorapi"
ownername = "polaronsolartech"

params = {"authtoken": authtoken, "scope": scope, "zc_ownername": ownername}
query_string = urllib.parse.urlencode(params)
reqUrl = url + "?" + query_string
try:
    with urllib.request.urlopen(reqUrl) as response:
        content = response.read().decode('utf-8')
        for line in csv.reader(content.splitlines()):
            with open('Records.csv', 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(line)
except urllib.error.HTTPError as error:
    print("Error Code: " + str(error.code))
