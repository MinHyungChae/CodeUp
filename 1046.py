# 합과 평균을 줄을 바꿔 출력한다.
# 평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.

a, b, c = input().split()

int_a = int(a)
int_b = int(b)
int_c = int(c)

sum_abc = int_a + int_b + int_c
print(sum_abc)
print("{0:.1f}".format(sum_abc/3))

