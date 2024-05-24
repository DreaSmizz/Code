import requests
import json

response = requests.get('http://localhost:8000')
print(response.text)