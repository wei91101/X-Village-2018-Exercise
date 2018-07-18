import requests
import json

url = 'https://www.metaweather.com/api/location/2306179/2018/7/18/'
response = requests.get(url)

# print(type(response.text))
# print(response.text)
j = json.loads(response.text)
#print(type(j))
for i in range (len(j)):
    x = j[i]['applicable_date']
    y = j[i]['weather_state_name']
    print(x,'weather is',y)

# #taipei = 2306179