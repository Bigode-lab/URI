anos = [int(x) for x in input().split()]
if ((abs(anos[0]+anos[1]) <= anos[2]) or(abs(anos[1]-anos[0]) == anos[2])):
    print('S')
else:
    print('N')