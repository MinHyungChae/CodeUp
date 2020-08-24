# 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

a, b = input().split()

if int(a) == 0 and int(b) == 0:
    print(1)
else:
    print(0)
