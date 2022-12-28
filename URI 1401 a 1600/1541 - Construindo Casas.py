n = [int(x) for x in input().split()]
while n[0] != 0:
    c = int(((n[0]*n[1]*100)/n[2])**0.5)
    print(c)
    n = [int(x) for x in input().split()]