# 등비수열의 n번째 항 출력

a1 = int(input('a1 입력 : '))
r = int(input('공비 입력 : '))
input_n = int(input('n 입력 : '))

n = 1
an = 0

while n <= input_n:
    if n == 1:
        an = a1
        print('{}번째 항의 값 : {}'.format(n, an))
        n += 1
        continue

    an *= r
    print('{}번째 항의 값 : {}'.format(n, an))
    n += 1


print('{}번째 항의 값 : {}'.format(input_n, an))