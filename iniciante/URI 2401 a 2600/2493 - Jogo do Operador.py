while True:
    try:
        n = int(input())
        l = []
        erraram = []
        for x in range(n):
            a = input().split(' ')
            c, d = a[1].split('=')
            l.append([a[0], c, d])

        for x in range(n):
            nome, equacao, operação = (str(x) for x in input().split(' '))
            if operação == '+':
                if int(l[int(equacao)-1][0]) + int(l[int(equacao)-1][1]) == int(l[int(equacao)-1][2]):
                    continue
                else:
                    erraram.append(nome)
            elif operação == '-':
                if int(l[int(equacao)-1][0]) - int(l[int(equacao)-1][1]) == int(l[int(equacao)-1][2]):
                    continue
                else:
                    erraram.append(nome)
            elif operação == '*':
                if int(l[int(equacao)-1][0]) * int(l[int(equacao)-1][1]) == int(l[int(equacao)-1][2]):
                    continue
                else:
                    erraram.append(nome)
        if len(erraram) == 0:
            print('You Shall All Pass!')
        elif len(erraram) == n:
            print('None Shall Pass!')
        else:
            erraram.sort()
            print(*erraram)
    except EOFError:
        break