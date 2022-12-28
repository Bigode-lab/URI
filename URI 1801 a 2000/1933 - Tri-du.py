a, b = (int(x) for x in input().split())
if a == b:
    print(a)
elif a != b:
    print(max(a, b))