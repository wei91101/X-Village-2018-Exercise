import json

f = open('music_show.json', 'r', encoding='utf-8')
# f.write(response.text)
j = json.load(f)
s = json.dumps(j, indent=4)
print(s)