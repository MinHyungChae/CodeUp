# 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
# 단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

# [true_value] if [condition] else [false_value] // 파이썬 지원

a, b = input().split()

print(int(a) if int(a) > int(b) else int(b))

