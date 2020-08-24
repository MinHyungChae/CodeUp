# [70000]
# [5000]
# [200]
# [50]
# [4]

original = input()
length = len(original) # 75254 -> 5

for i in range(0, 5):
    print("["+original[i]+'0'*(length-1-i)+"]")