'''
1. 10진수 -> n진수 변환

2진수 : binary : bin()
8진수 : octal : oct()
16진수 : Hexadecimal : hex()

변환결화는 문자열!
'''
dNum = 30
print('2진수 : {}'.format(bin(dNum)))  # 0b : 2진수
print('8진수 : {}'.format(oct(dNum)))  # 0o : 8진수
print('16진수 : {}'.format(hex(dNum))) # 0x : 16진수
print('\n')
print('{0:#b}, {0:#o}, {0:#x}'.format(dNum))
print('\n')
print('2진수 : {}'.format(format(dNum, 'b')))
print('8진수 : {}'.format(format(dNum, 'o')))
print('16진수 : {}'.format(format(dNum, 'x')))

