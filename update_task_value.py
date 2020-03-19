import urllib.parse
import urllib.request
import json

url = "https://projectsapi.zoho.com/restapi/portal/polarongr/projects/1337133000001584023/tasks/1337133000001584125/"
authtoken = "7c62575a85aa03a9a974f707615f8e5c"
params = {"authtoken": authtoken, "custom_fields": {"UDF_DATE1": "08-09-2020"}}
query_string = urllib.parse.urlencode(params).encode()
req =  urllib.request.Request(url, data=query_string)
try:
    with urllib.request.urlopen( req ) as response:
        response_data = json.loads(response.read())
        print(response_data)
except urllib.error.HTTPError as error:
    print("Error: " + str(error))