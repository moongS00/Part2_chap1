# 최소공배수
# 두개의 수에 대한 최소공배수를 구한 후, 다시 세번째 수의 공배수를 구한다.

n1 = int(input("1보다 큰 정수 입력 : "))
n2 = int(input("1보다 큰 정수 입력 : "))
n3 = int(input("1보다 큰 정수 입력 : "))

max_n = 0

for i in range(1, (n1 + 1)):
    if n1 % i == 0 and n2 % i == 0:
        max_n = i

min_n = int((n1 * n2) //max_n)

print('{}, {}의 최대공약수 : {}'.format(n1, n2, max_n))
print('{}, {}의 최소공배수 : {}'.format(n1, n2, min_n))


new_n = min_n
new_x = 0
for i in range(1, (new_n + 1)):
    if n3 % i == 0 and new_n % i == 0:
        new_x = i

new_i = int((new_n * n3) //new_x)

print('{}, {}의 최대공약수 : {}'.format(new_n, n3, new_x))
print('{}, {}, {}의 최소공배수 : {}'.format(n1, n2, n3, new_i))

