# 수열의 n번째 항을 출력


a1 = int(input('a1 입력 : '))
d = int(input('공차 입력 : '))
nn = int(input('n 입력 : '))

n = 1
an = 0

while n <= nn:
    if n == 1:
        an = a1
        print('{}번째 항의 값 : {}'.format(n, an))
        n += 1
        continue

    an += d
    print('{}번째 항의 값 : {}'.format(n, an))
    n += 1

print('{}번째 항의 값 : {}'.format(nn, an))
