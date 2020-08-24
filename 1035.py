# 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

a = input()
hex_a = int(a, 16)
print(oct(hex_a)[2:])