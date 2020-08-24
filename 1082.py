# 입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다. 결과도 16진수로 

a = input()

for i in range(1, 16):
    result = '{0:x}'.format(int(a, 16) * i)
    print(a + '*' + '{0:x}'.format(i).upper() + '=' + result.upper())
    
