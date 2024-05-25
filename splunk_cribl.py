# Andrea Smith
# Cribl Assessment
# May 2024 | cribl.py
# Program Requirements
## Grab dataset from public url (github)
## Change from csv format to json
## send to cribl stream
## from cribl stream send to http s-word for searching


# Required packages for script to work
import json
import requests
import pandas as pd



# Send requests for CSV file
stock = pd.read_csv("https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv")
#Convert to json format for ingestion
stocks_json = stock.to_json(orient='records')
# My lab splunk 
url = 'http://localhost:8000'
data = stocks_json
splunk_headers = {'Authorization': 'Splunk <token>','Content-Type': 'application/json'}
response = requests.post(url, headers=splunk_headers, json=json.dumps(data), verify=False )
print(response.status_code)