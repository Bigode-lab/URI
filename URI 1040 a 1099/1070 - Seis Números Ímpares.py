n = int(input())
a =  n%2
if a == 0:
    n += 1
    for x in range(6):
        print(n)
        n += 2
elif a != 0:
    for x in range(6):
        print(n)
        n += 2