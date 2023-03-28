n = int(input())
for x in range(n):
    a = input()
    if a[0] == a[-1]:
        print(int(a[0])*int(a[-1]))
    elif a[1].isupper():
        print(int(a[-1])-int(a[0]))
    else:
        print(int(a[0]) + int(a[-1]))