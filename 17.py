# 등비수열의 합 출력
a1 = int(input('a1 입력 : '))
r = int(input('공비 입력 : '))
input_n = int(input('n 입력 : '))

n = 1
an = 0
sn = 0

while n <= input_n:
    if n == 1:
        an = a1
        sn += an
        print('{}번째 항까지의 합 : {}'.format(n, sn))
        n += 1
        continue

    an *= r
    sn += an
    print('{}번째 항까지의 합 : {}'.format(n, sn))
    n += 1

sum_n = a1 *((1 - (r ** input_n)) / (1 - r))
print('{}번째 항까지의 합 : {}'.format(input_n, sum_n))