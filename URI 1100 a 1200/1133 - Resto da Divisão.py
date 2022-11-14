a = int(input())
b = int(input())
if a < b:
    while a < b:
        a += 1
        if a < b:
            t = a%5
            if t == 2 or t == 3:
                print(a)
elif a > b:
    while a > b:
        b += 1
        if a > b:
            t = b%5
            if t == 2 or t == 3:
                print(b)