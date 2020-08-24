# input -1 값 까지만. 조합. 전체 조합 개수

a, b, c = input().split()

for i in range(0, int(a)):
    for j in range(0, int(b)):
        for k in range(0, int(c)):
            print(i, j, k)

print(int(a)*int(b)*int(c))
