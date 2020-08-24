# input : 44100 16 2 10

a_input = map(int, input().split())
result = 1
mb = 8*1024*1024

for a in a_input:
    result *= a

print('{0:.1f}'.format(result/mb) + ' MB')


