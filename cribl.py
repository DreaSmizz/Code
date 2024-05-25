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
splunk_headers = {'Authorization': 'Splunk ffce3d95-2625-4e01-ab6a-f153fb9aae8c','Content-Type': 'application/json'}
response = requests.post(url, headers=splunk_headers, json=json.dumps(data), verify=False )
print(response.status_code)






#import csv
#print(response.content)
#splunk = SplunkSender(**splunk_conf)
#from splunk_data_sender import SplunkSender
#splunk_conf = {
#    'endpoint':'http://localhost',
#    'port':'8000',
#    'token':'424e510f-631d-4da3-b0d6-bbcdc15fb91a',
#}


#connection = httplib2.HTTPSConnection('localhosts:8088')
#connection.request('POST', url, json.dumps(data), headers)

#splunk = SplunkSender(**splunk_conf)

#cribl_stream = 'https://default.main.infallible-miatselski-783se76.cribl.cloud:10200/api/v1/system/outputs/infallible-miatselski-783se76'
#cribl_stream_url = 'http://192.168.4.198:9000/'
#response = requests.posts('https://192.168.4.198:900/api/v1', json=stocks_json)
#curl -X POST https://192.168.4.198:9000/api/v1/auth/login -H "Content-Type: stocks_json" -d '{"username":"admin","password":"J@deNyla2018"}'











#stock_csv = requests.get('https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv')
#url = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/main/data/constituents.csv'
#jsondict=json.loads(stocks_json)
#first = list(jsondict)[0]
#print(first)


# If dataset no longer available, send error message
#if stock_csv.status_code == 200:
#    csv_content = stock_csv.content
#    print(csv_content)
    #csv_file = open('stock.csv', 'wb')
#    csv_reader = csv.DictReader(BytesIO(csv_content))
#    json_data = json.dumps(list(csv_reader))
#    print(json_data)
    #csv_file.write(csv_content)


    #csv_file.close()
        



#stocks = pandas.read_csv('csv_content')
#json_stock_data = json.dumps(stocks, indent=4)
#print(json_stock_data)
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


