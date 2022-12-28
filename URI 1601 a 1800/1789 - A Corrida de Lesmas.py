while True:
    try:
        n = int(input())
        l = [int(x) for x in input().split()]
        a = max(l)
        if a < 10:
            print('1')
        elif a >= 20:
            print('3')
        else:
            print('2')
    except EOFError:
        break