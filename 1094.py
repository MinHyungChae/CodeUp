# 10
# 10 4 2 3 6 6 7 9 8 5

a = int(input())
b = input().split()

for i in range(0, a):
    print(b[a-i-1], end=" ")
