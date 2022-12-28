a, b = (int(x) for x in input().split())
if b < 0:
    print(f'{(a//-b)*-1} {a%-b}')
else:
    print(f'{a//b} {a%b}')