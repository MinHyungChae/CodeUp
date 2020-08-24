#5 5
#3
#2 0 1 1 길이 방향 좌표
#3 1 2 3
#4 1 2 5

a_length, b_length = list(map(int,input().split()))
n = int(input())

arr = [[0 for j in range(b_length)] for i in range(a_length)]

for i in range(n):
    length, d, x, y = map(int, input().split())
    for j in range(length):
        if d == 0:
            arr[x-1][y-1+j] = 1
        else:
            arr[x-1+j][y-1] = 1
            
for i in range(a_length):
    for j in range(b_length):
        print(arr[i][j], end=" ")
    print('')
