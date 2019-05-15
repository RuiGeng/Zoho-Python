import urllib.parse
import urllib.request
import json
import csv
import os
import time

# Remove file
if os.path.exists('all_task.csv'):
    os.remove('all_task.csv')

# Initial value
authtoken = "7c62575a85aa03a9a974f707615f8e5c"
params = {"authtoken": authtoken}
query_string = urllib.parse.urlencode(params)
title_list = ["Project ID", "Task Name",
              "Task ID", "Duration", "Successor", "Predecessor", "Owner ID"]

with open('all_task.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(title_list)

# Remove file
if os.path.exists('all_project.csv'):
    with open('all_project.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            time.sleep(2)
            task_url = row[3]
            reqUrl = task_url + "?" + query_string
            try:
                with urllib.request.urlopen(reqUrl) as response:
                    response_data = json.loads(response.read())
                    for t in response_data['tasks']:
                        row_list = list()
                        successors = ""
                        predecesses = ""
                        ownerid_list = list()
                        owner_id = ""

                        row_list.append(row[1])
                        row_list.append(t['name'])
                        row_list.append(t['id_string'])
                        row_list.append(t['duration'])
                        if t['dependency'].get('successor') is not None:
                            successors = ','.join(
                                t['dependency'].get('successor'))
                        if t['dependency'].get('predecessor') is not None:
                            predecesses = ','.join(
                                t['dependency'].get('predecessor'))
                        row_list.append(successors)
                        row_list.append(predecesses)
                        if t['details'].get('owners') is not None:
                            for o in t['details'].get('owners'):
                                if 'id' in o:
                                    ownerid_list.append(o.get('id'))
                        owner_id = ','.join(ownerid_list)
                        row_list.append(owner_id)
                        with open('all_task.csv', 'a') as csv_file:
                            writer = csv.writer(csv_file)
                            writer.writerow(row_list)
            except urllib.error.HTTPError as error:
                print("Get Error Code: " + str(error.code))
