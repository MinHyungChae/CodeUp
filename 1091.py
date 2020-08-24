# 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열이다.
# a(시작) m(곱) d(더할) n(몇번)

A, M, D, N = input().split()
a = int(A)
m = int(M)
d = int(D)
n = int(N)

for i in range(n-1):
    a = a * m + d
    
print(a)

