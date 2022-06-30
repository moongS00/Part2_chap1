# Sn 출력하기

a1 = int(input('a1 입력 : '))
d = int(input('공차 입력 : '))
nn = int(input('n 입력 : '))

n = 1
an = 0
sn = 0

while n <= nn:
    if n == 1:
        an = a1
        print('{}번째 항까지의 합 : {}'.format(n, an))
        sn += an
        n += 1
        continue

    an += d
    sn += an
    print('{}번째 항까지의 합 : {}'.format(n, sn))
    n += 1

sumN = int((nn * (a1 + an)) / 2)
print('{}번째 항까지의 합: {}'.format(nn, sumN))