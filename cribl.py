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
import csv
import requests
from splunk_data_sender import SplunkSender
import pandas

splunk_conf = {
    #'endpoint' = "https://default.main.infallible-miatselski-783se76.cribl.cloud:10200",
    #'endpoint':'https://http-input-prd-p-t9vwy.splunkcloud.com:8088/services/collector',
    #hec_token = 'e8983479-46a4-5817-aa6e-e0251328bc79'
    #'endpoint':'si-i-0403e82113a9640bd.prd-p-t9vwy.splunkcloud.com',
    'endpoint':'http://192.168.4.198',
    'port':'9000',
    'token':'424e510f-631d-4da3-b0d6-bbcdc15fb91a',
}

splunk = SplunkSender(**splunk_conf)

#cribl_stream = 'https://default.main.infallible-miatselski-783se76.cribl.cloud:10200/api/v1/system/outputs/infallible-miatselski-783se76'
#cribl_stream_url = 'http://192.168.4.198:9000/'


# Send requests for CSV file
stock_csv = requests.get('https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv')
# If dataset no longer available, send error message
if stock_csv.status_code == 200:
    csv_content = stock_csv.content
    csv_reader = csv.DictReader(csv_content)
    #stocks = pandas.read_csv('csv_content')

#json_stock_data = json.dumps(stocks, indent=4)
#print(json_stock_data)
    csv_file = open('stock.csv', 'wb')
    csv_file.write(csv_content)
    csv_file.close()
        

#print(stock_csv.status_code)
# Convert CSV data to JSON so it can be ingested
#with open('stock_csv', mode='r') as file:
#    csv_read = csv.DictReader(stock_csv)
#    csv_list = []
#    for row in csv_read:
#        csv_list.append(row)

#for data in csv_list:
#    print(csv)


#stock_csv = csv.DictReader(stock_csv.text.splitlines())
#headers = stock_csv.fieldnames
#json_data = [dict(zip(headers, row)) for row in stock_csv]
#payload = [json_data]



#cribl = requests.put('http://192.168.4.198:9000/', data=payload)
#print(cribl.status_code)
# Validating data is showing as json
# print(json_data)
#event = requests.post(splunk_conf, json=json_data, headers=headers, verify=False)
#print(event.json())


#424e510f-631d-4da3-b0d6-bbcdc15fb91a



#https://http-inputs-<host>.splunkcloud.com:<port>/<endpoint>


