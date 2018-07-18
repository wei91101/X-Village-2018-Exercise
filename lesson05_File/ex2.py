import csv

with open ('AQI_20180717094036.csv','r',encoding='utf-8-sig') as c:
    reader = csv.reader(c)
    count1 = 0
    for x in reader:
        count1 = count1 + 1
    #print(count1)

    c.seek(0)
    a = []
    b = []
    i = 0

    for row in reader:
        #print(row[1],row[2])
        if(row[2] != 'AQI'):
            a.append(int(row[2]))
            b.append(row[1])
            #print(b)
            #print(a)
            #print(min(a))
    count = 0
    for i in range (count1):
        if(a[i] == min(a)):
            #print (count)
            break
        count = count + 1
    #print(a[68],b[68])
    print(b[count],'空氣最好，AQI是',a[count])