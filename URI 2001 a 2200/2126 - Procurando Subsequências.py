caso = 0
while True:
    try:
        caso += 1
        n = input()
        n1 = input()
        indice = 0
        ocorrencia = 0
        for s in n1:
            if s == n[0] and ((indice + len(n)) <= len(n1)):
                if n1[indice:(indice + len(n))] == n:
                    pos = indice
                    ocorrencia += 1
            indice += 1
        if ocorrencia != 0:
            print(f'Caso #{caso}:\nQtd.Subsequencias: {ocorrencia}\nPos: {pos+1}')
            print('')
        else:
            print(f'Caso #{caso}:')
            print('Nao existe subsequencia')
            print('')
    except EOFError:
        break