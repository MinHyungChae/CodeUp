# 최소 공배수 구하는 문제
from math import gcd

def lcm(x, y):
    return x*y // gcd(x, y)

A, B, C = input().split()

a = int(A)
b = int(B)
c = int(C)

result = lcm(lcm(a,b), c)
print(result)


