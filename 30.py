# 1. 박스에 '꽝'이 적힌 종이가 4장 있고, '선물'이 적힌 종이가 3자이 있을 때,
# 파이썬을 이용해 '꽝' 2장과 '선물' 1장을 뽑을 확률을 출력해하

gg = int(input('총 카드 개수 입력 : '))
pp = int(input('뽑을 카드 개수 입력 : '))
sample1 = 1
sample2 = 1
sample3 = 1

for i in range(gg, (gg-pp), -1):
    sample1 *= i


for i in range(pp, 0, -1):
    sample2 *= i


sample3 = int(sample1 / sample2)
print('sample : {}'.format(sample3))


numN = int(input('numN 입력 : '))
numR = int(input('numR 입력 : '))

resultP = 1
resultR = 1
resultC = 1

for i in range(numN, (numN-numR), -1):
    resultP *= i


for i in range(numR, 0, -1):
    resultR *= i

resultC = int(resultP / resultR)
print('event1 : {}'.format(resultC))



numN2 = int(input('numN 입력 : '))
numR2 = int(input('numR 입력 : '))

resultP2 = 1
resultR2 = 1
resultC2 = 1

for i in range(numN2, (numN2-numR2), -1):
    resultP2 *= i


for i in range(numR2, 0, -1):
    resultR2 *= i

resultC2 = int(resultP2 / resultR2)
print('event2 : {}'.format(resultC2))


prob = ((resultC * resultC2) / sample3) * 100
probability = round(prob, 2)
print('probability : {}%'.format(probability))