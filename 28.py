# 조합

numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

resultP = 1
resultR = 1
resultC = 1

for i in range(numN, (numN-numR), -1):
    print('n : {}'.format(i))
    resultP *= i

print('resultP : {}'.format(resultP))


for i in range(numR, 0, -1):
    print('n : {}'.format(i))
    resultR *= i

print('resultP : {}'.format(resultR))

resultC = int(resultP / resultR)
print('resultP : {}'.format(resultC))

