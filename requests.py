import requests
import json

url ='http://192.168.4.198:9000/'

data = {'day': 'thursday'}

response = requests.post(url, data=data)