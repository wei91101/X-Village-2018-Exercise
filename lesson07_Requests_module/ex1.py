import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response = requests.get(url)

f = open('music_show.json','w',encoding='utf-8')
f.write(response.text)
f.close()
#print(response.text)
f = open('music_show.json', encoding='utf-8')
# f.write(response.text)

j = json.load(f)
print(len(j))
print(type(j))
f = open ('music_show.txt','w',encoding='utf-8')
for i in range (len(j)):
    x = j[i]['title']
    y = j[i]['startDate']
    z = j[i]['endDate']
    #print(x,y,z)
    w = x + y + '~' + z
    #print(w)
    f.write(w)
    f.write('\n')
