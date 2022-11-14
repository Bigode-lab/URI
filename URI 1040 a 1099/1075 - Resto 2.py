n = int(input())
a = 0
while a < 10000:
    c = a%n
    if c == 2:
        print(a)
    a += 1