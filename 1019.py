# 2013.8.5
a = input()
ymd = a.split(".")
if len(ymd[0]) != 4:
    count = 4 - len(ymd[0])
    ymd[0] = str('0')*count + str(ymd[0])
if len(ymd[1]) == 1:
    ymd[1] = '0'+str(ymd[1])
if len(ymd[2]) == 1:
    ymd[2] = '0' + str(ymd[2])
print(ymd[0]+'.'+ymd[1]+'.'+ymd[2])