# 세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

a, b, c = map(int, input().split())

list_abc = [a, b, c]

for abc in list_abc:
    if abc%2 == 0:
        print(abc)
