n = int(input())
for x in range(n):
    n1 = int(input())
    a = n1%2
    if a == 0 and n1 <0:
        print('EVEN NEGATIVE')
    elif a == 0 and n1 >0:
        print('EVEN POSITIVE')
    elif a != 0 and n1 < 0:
        print('ODD NEGATIVE')
    elif a != 0 and n1 > 0:
        print('ODD POSITIVE')
    else:
        print('NULL')