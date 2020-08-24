# 10
# 10 4 2 3 6 6 7 9 8 5

a = input()
b = input().split()

min = int(b[0])

for i in b:
    if (int(i)<= min):
        min = int(i)

print(min)
