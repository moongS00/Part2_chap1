# 소인수 분해

ipn = int(input("1보다 큰 정수 입력 : "))

n=2
while n <= ipn:
    if ipn % n == 0:
        print('소인수 : {}'.format(n))
        ipn /= n

    else:
        n += 1
