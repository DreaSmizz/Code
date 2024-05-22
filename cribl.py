import json
import csv
import requests
import splunklib

#cribl_instance = "https://default.main.infallible-miatselski-783se76.cribl.cloud:10200"
splunk_instance ="https://http-input-prd-p-t9vwy.splunkcloud.com:8088/services/collector"
#hec_token = 'e8983479-46a4-5817-aa6e-e0251328bc79'
splunk_token = 'c368c603-a8a5-4d78-b950-f1114f286638'

headers = {
    'Authorization': splunk_instance + splunk_token,
    'Splunk-Request': 'aaaaaaa-6789-rrrr'
}
# Send requests for CSV file
stock_csv = requests.get('https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv')
# If dataset no longer available, send error message
if stock_csv.status_code != 200:
    print("Dataset no longer available.")
# Convert CSV data to JSON so it can be ingested
stock_csv = csv.DictReader(stock_csv.text.splitlines())
headers = stock_csv.fieldnames
json_data = [dict(zip(headers, row)) for row in stock_csv]
# Validating data is showing as json
# print(json_data)
event = requests.post(splunk_instance, json=json_data, headers=headers, verify=False)
print(event.json())






#https://http-inputs-<host>.splunkcloud.com:<port>/<endpoint>