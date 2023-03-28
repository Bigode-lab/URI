while True:
    try:
        direita = {}
        esquerda = {}
        botas = int(input())
        for x in range(botas):
            tamanho, lado = (str(x) for x in input().split(' '))
            if lado == 'D':
                if int(tamanho) not in direita:
                    direita[int(tamanho)] = 1
                    c = int(tamanho)
                else:
                    direita[int(tamanho)] += 1
            elif lado == 'E':
                if int(tamanho) not in esquerda:
                    esquerda[int(tamanho)] = 1
                else:
                    esquerda[int(tamanho)] += 1
        pares = 0
        for x in range(29,64,1):
            if x in direita and x in esquerda:
                pares += min(direita[x], esquerda[x])
        print(pares)
    except EOFError:
        break
