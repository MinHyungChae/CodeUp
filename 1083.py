# input : 9 result: 1 2 X 4 5 X 7 8 X

a = int(input())

for i in range(1, a+1):
    if i%3 ==0:
        print('X', end=" ", flush = True)
    else: 
        print(i, end=" ")
