f = open('note.txt','w')
f = open('note.txt','r+')
date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')
f.write(date)
f.write('\n')
f.write(event)
f.write('\n')
f.write(description)