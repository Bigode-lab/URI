grito = 0
soma  = 0
while grito < 3:
    s = input()
    if s == 'caw caw':
        grito += 1
        print(soma)
        soma = 0
    else:
        for x in range(3):
            if s[x] == '*' and x == 0:
                soma += 4
            if s [x] == '*' and x == 1:
                soma += 2
            if s [x] == '*' and x == 2:
                soma += 1