# 7 4 2 3 0 1 5 6 9 10 8

input_array = map(int, input().split())
for item in input_array:
    if item == 0:
        break
    else:
        print(item)
