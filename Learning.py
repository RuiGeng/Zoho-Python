import urllib.parse
import urllib.request
import json
import csv
import os
import time

# Initial value
id_cancelled = 1337133000001709097
id_closed = 1337133000000016071
id_inprogress = 1337133000000553253
id_open = 1337133000000016068
authtoken = "7c62575a85aa03a9a974f707615f8e5c"
params = {"authtoken": authtoken}
query_string = urllib.parse.urlencode(params)

# Remove file
if os.path.exists('all_project.csv'):
    with open('all_project.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if row[2] == "Cancelled":
                url = row[3]
                reqUrl = url + "?" + query_string
                try:
                    with urllib.request.urlopen( reqUrl ) as response:
                        response_data = json.loads(response.read())
                        for t in response_data['tasks']:
                            if(t['status'].get('name') == "In process" or t['status'].get('name') == "Open"):
                                post_params = {"authtoken": authtoken, "custom_status": id_cancelled}
                                post_string = urllib.parse.urlencode(post_params).encode()
                                post_url = url + t['id_string'] + "/"
                                post_req =  urllib.request.Request(post_url, data=post_string)
                                print(post_url)
                                try:
                                    with urllib.request.urlopen( post_req ) as response:
                                        response_data = json.loads(response.read())
                                        print(response_data)
                                        time.sleep(1)
                                except urllib.error.HTTPError as error:
                                    print("Post Error Code: " + error.code)
                except urllib.error.HTTPError as error:
                    print("Get Error Code: " + str(error.code))