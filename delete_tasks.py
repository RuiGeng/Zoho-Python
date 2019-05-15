import os
import csv
import urllib.parse
import urllib.request
import json
import time

def deleteTask(projectId, taskId):
    baseUrl = "https://projectsapi.zoho.com/restapi/portal/polarongr/projects/"
    deleteUrl = baseUrl + str(projectId) + "/" + "tasks/" + str(taskId) + "/"
    params = {"authtoken": "7c62575a85aa03a9a974f707615f8e5c"}
    query_string = urllib.parse.urlencode(params)
    url = deleteUrl + "?" + query_string
    req = urllib.request.Request( url, method='DELETE')

    try:
        response = urllib.request.urlopen(req)
        print("Success: " + response.read().decode('utf8'))
    except urllib.error.HTTPError as error:
        print("Error: " + error.code)

with open("All Delete Tasks_1.csv", "r") as csvFile:
    reader = csv.reader (csvFile)
    for row in reader:
        project_id =  row[0]
        task_id = row[1]
        deleteTask(project_id, task_id)
        time.sleep(10)