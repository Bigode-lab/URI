r = 0
a = int(input())
b = int(input())
if a > b:
    while b <= a: 
        t = b%13
        if t != 0:
            r += b
            b += 1
        else:
            b += 1
elif b > a:
    while a <= b: 
        t = a%13
        if t != 0:
            r += a
            a += 1
        else:
            a += 1
print(r)