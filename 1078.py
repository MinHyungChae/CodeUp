# 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

a = int(input())
e_sum = 0

for i in range(1, a+1):
    if(i%2 == 0):
        e_sum += i
print(e_sum)
