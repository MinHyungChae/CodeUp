# 좌표는 1~19. 첫줄: 갯수 둘째부터 그 이후: 좌표

n=int(input())

a=[[0 for j in range(20)] for i in range(20)]
for i in range(n):
    x,y=list(map(int,(input().split())))
    a[x][y]=1   
    
for j in range(1,20):
    for k in range(1,20):
        print(a[j][k],end=' ')
    print('')

