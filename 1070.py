# 월 : 계절 이름
#12, 1, 2 : winter
#  3, 4, 5 : spring
#  6, 7, 8 : summer
#  9, 10, 11 : fall

# python 에는 switch case 문이 없다. if 문이나 dictionary 를 사용해서 대체한다.

a = int(input())

if a == 12 or a == 1 or a ==2:
    print('winter')
elif a == 3 or a == 4 or a == 5:
    print('spring')
elif a == 6 or a ==7 or a == 8:
    print('summer')
else:
    print('fall')


