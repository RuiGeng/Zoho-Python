import urllib.parse
import urllib.request
import json
import csv
import os

# Remove file
if os.path.exists('all_project.csv'):
    os.remove('all_project.csv')

# Initial value
has_projects = True
start_index = 1
title_list = ["Project Name", "Project ID", "Project Status", "Task URL"]

"""
with open('all_project.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(title_list)
"""

while has_projects:
    url = "https://projectsapi.zoho.com/restapi/portal/polarongr/projects/"
    authtoken = "7c62575a85aa03a9a974f707615f8e5c"
    params = {"authtoken": authtoken, "index": start_index, "range": 100}
    query_string = urllib.parse.urlencode(params)
    reqUrl = url + "?" + query_string
    p_count = 0
    try:
        with urllib.request.urlopen(reqUrl) as response:
            response_data = json.loads(response.read())
            for p in response_data['projects']:
                p_count += 1
                start_index += 1
                row_list = list()
                project_status = ""
                for cf in p['custom_fields']:
                    for ps in cf:
                        if(ps == "Project Status"):
                            project_status = cf[ps]
                row_list.append(p["name"].strip())
                row_list.append(p["id_string"].strip())
                row_list.append(project_status)
                row_list.append(p["link"].get("task").get("url").strip())
                with open('all_project.csv', 'a') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(row_list)
                    # csv_file.close()
            if(p_count >= 100):
                has_projects = True
            else:
                has_projects = False
    except urllib.error.HTTPError as error:
        print("Error Code: " + str(error.code))
