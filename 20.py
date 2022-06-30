# 계차수열의 항 출력

in_a1 = int(input('a1 입력 : '))
in_an = int(input('n 입력 : '))

in_b1 = int(input('b1 입력 : '))
in_bd = int(input('bn의 공차 입력 : '))

val_an = 0
val_bn = 0
n = 1

while n <= in_an:

    if n == 1:
        val_an = in_a1
        val_bn = in_b1
        print('an의 {}번째 항의 값 : {}'.format(n, val_an))
        print('bn의 {}번째 항의 값 : {}'.format(n, val_bn))
        n += 1
        continue

    val_an += val_bn
    val_bn += in_bd
    print('an의 {}번째 항의 값 : {}'.format(n, val_an))
    print('bn의 {}번째 항의 값 : {}'.format(n, val_bn))
    n += 1

print('\n')
print('an의 {}번째 항의 값 : {}'.format(in_an, val_an))
print('bn의 {}번째 항의 값 : {}'.format(in_an, val_bn))

