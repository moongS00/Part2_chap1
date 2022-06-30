# 최대공약수
'''
n1 = int(input("1보다 큰 정수 입력 : "))
n2 = int(input("1보다 큰 정수 입력 : "))
n3 = int(input("1보다 큰 정수 입력 : "))

max_n = 0

for i in range(1, (n1 + 1)):
    if n1 % i == 0 and n2 % i == 0 and n3 % i == 0:
        print('공약수 : {}'.format(i))
        max_n = i



print('최대공약수 : {}'.format(max_n))
'''


# 유클리드 호제법을 이용해 최대공약수 찾기
n1 = int(input("1보다 큰 정수 입력 : "))
n2 = int(input("1보다 큰 정수 입력 : "))

tem1 = n1
tem2 = n2

while tem2 >0:
    tem = tem2
    tem2 = tem1 % tem2
    tem1 = tem

print('{}, {}의 최대공약수 : {}'.format(n1, n2, tem1))

for n in range(1, (tem1 + 1)):
    if tem1 % n == 0:
        print('{}, {}의 공약수 : {}'.format(n1, n2, n))
