# 두 개의 참(1) 또는 거짓(0)이 입력될 때,
# 참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.

a, b = input().split()
xor_answer = bool(int(a)^int(b))

print(int(not xor_answer))
