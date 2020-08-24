# initial
a = [[0 for j in range(20)]for i in range(20)]

for i in range(19):
    x = list(map(int, input().split()))
    for j in range(19):
        a[i+1][j+1] = x[j]
        
n = int(input())

for v in range(n):
    v1, v2 = map(int, input().split())
    for m in range(1, 20):
        if a[v1][m] == 0:
            a[v1][m] = 1
        else:
            a[v1][m] = 0
        if a[m][v2] == 0:
            a[m][v2] = 1
        else:
            a[m][v2] = 0
            

for i in range(1, 20):
    for j in range(1, 20):
        print(a[i][j], end=" ")
    print('')

