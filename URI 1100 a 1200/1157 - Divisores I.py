n = int(input())
for x in range(n):
    a = n%(x+1)
    if a == 0:
        print(x+1)