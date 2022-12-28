n = int(input())
for x in range(n):
    print('{} {} {}'.format((x+1), ((x+1)**2), ((x+1)**3)))
    print('{} {} {}'.format((x+1), (((x+1)**2)+1), (((x+1)**3)+1)))