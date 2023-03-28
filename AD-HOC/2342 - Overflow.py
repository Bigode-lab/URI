limite = int(input())
n1, sinal, n2 = (str(x) for x in input().split())
if sinal == '*':
    if int(limite) >= int(n1) * int(n2):
        print('OK')
    else:
        print('OVERFLOW')
else:
    if int(limite) >= int(n1) + int(n2):
        print('OK')
    else:
        print('OVERFLOW')