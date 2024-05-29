import json

import requests

BASE = "http://127.0.0.1:5000/"
headers = {'Content-Type': 'application/json',
           'Accept-Charset': 'UTF-8'}
data = [{"likes": 10, "name": "Tim", "views": 100000},
        {"likes": 10000, "name": "How to make REST API", "views": 80000},
        {"likes": 35, "name": "Tim", "views": 2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i], headers=headers)
    print(response.json())

input()
response = requests.get(BASE + "video/2")
print(response.json())