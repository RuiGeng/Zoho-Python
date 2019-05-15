import urllib.parse
import urllib.request
import json

url = "https://projectsapi.zoho.com/restapi/portals/"
authtoken = "7c62575a85aa03a9a974f707615f8e5c"
params = {"authtoken": authtoken}
query_string = urllib.parse.urlencode(params)
reqUrl = url + "?" + query_string

try:
    with urllib.request.urlopen( reqUrl ) as response:
        response_data = json.loads(response.read())
        print(response_data)
except urllib.error.HTTPError as error:
    print("Error Code: " + str(error.code))