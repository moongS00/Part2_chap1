# 약수 : 나머지가 0인 숫자를 찾는다
'''
ipn = int(input("0보다 큰 정수 입력 : "))

for num in range(1, ipn+1):
    if ipn % num == 0:
        print('{}의 약수 : {}'.format(ipn, num))

'''

# 소수
ipn = int(input("0보다 큰 정수 입력 : "))

for i in range(2, ipn+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break


    if flag:
        print('{} : 소수'.format(i))
    else:
        print('{} : \t\t합성수'.format(i))


