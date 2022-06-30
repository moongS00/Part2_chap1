# 군 수열

inputN = int(input('n항 입력 : '))

n = 1
nCnt = 1
searchN = 0

flag = True
while flag:
    for i in range(1, (n + 1)):
        if i == n:
            print('{}'.format(i), end='')
        else:
            print('{}'.format(i), end='')

        nCnt += 1

        if nCnt > inputN:
            searchN = i
            flag = False
            break

    print()
    n += 1


print('{}항 : {}'.format(inputN, searchN))