'''
섬마을에 배 3대가 다음 주기로 입항한다고 할 때, 모든 배가 입항하는 날짜를 계산해보자
배1: 3일
배2: 4일
배3: 5일
'''

sh1 = 3
sh2 = 4
sh3 = 5
n_max = 0

for i in range(1, (sh1 + 1)):
    if sh1 % i == 0 and sh2 % i == 0:
        n_max = i

n_min = (sh1 * sh2 )// n_max
print('{}, {}의 최대공약수 : {}'.format(sh1, sh2, n_max))
print('{}, {}의 최소공배수 : {}'.format(sh1, sh2, n_min))


un = n_min
u_max = 0

for i in range(1, (n_max + 1)):
    if sh3 % i == 0 and un % i == 0:
        u_max = i


u_min = int((sh3 * un) // u_max)
print('{}, {}의 최대공약수 : {}'.format(un, sh3, u_max))
print('{}, {}, {}의 최소공배수 : {}'.format(sh1, sh2, sh3, u_min))

print('{}일마다 모든 선박이 입항합니다.'.format(u_min))

