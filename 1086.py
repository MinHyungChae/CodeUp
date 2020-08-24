a, b, c=input().split()

W=int(a)
H=int(b)
B=int(c)

print('{0:.2f} MB'.format(W*H*B/8/1024/1024))

