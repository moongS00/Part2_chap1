# 순열

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))
res = 1

for n in range(numN, (numN-numR), -1):
    print('n : {}'.format(n))
    res *= n

print('result : {}'.format(res))


# 월순열
n = int(input('친구 수 입력 : '))
result = 1

for i in range(1, n):
    result *= i

print('result : {}'.format(result))
