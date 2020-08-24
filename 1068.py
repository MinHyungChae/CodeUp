# 점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.
#점수 범위 : 평가
# 90 ~ 100 : A
# 70 ~ 89 : B
# 40 ~ 69 : C
# 0 ~ 39 : D

a = int(input())
if a >= 90 and a <= 100:
    print('A')
elif a >= 70 and a <= 89:
    print('B')
elif a>= 40 and a<= 69:
    print('C')
else:
    print('D')
