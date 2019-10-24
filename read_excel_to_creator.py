import pandas as pd
import urllib.parse
import urllib.request
import json

# URL Format
# https://creator.zoho.com/api/<ownername>/<format>/<applicationName>/view/<viewName>/record/update

url = "https://creator.zoho.com/api/polaronsolartech/json/polaron-reference-data/view/Deal_and_Projects_Report/record/update"
authtoken = "411ec6b991ed77bb876b2c78dc2659e5"
scope = "creatorapi"
criteria = "Project_ID=="

df = pd.read_excel('/Users/ruigeng/Downloads/Projects.xls',sheet_name='Sheet1')
for i in df.index:
    projectID = df['Project ID'][i]
    name=df['Project Name'][i]
    criteria = "Project_ID==" + str(projectID)
    params = {"authtoken": authtoken, "scope": scope, "criteria": criteria, "Accounting_Identity": name}
    query_string = urllib.parse.urlencode(params).encode()
    req =  urllib.request.Request(url, data=query_string)
    try:
        with urllib.request.urlopen( req ) as response:
            response_data = json.loads(response.read())
            print(response_data)
    except urllib.error.HTTPError as error:
        print("Error: " + str(error))