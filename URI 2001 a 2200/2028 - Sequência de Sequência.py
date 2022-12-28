caso = 1
while True:
    try:
        n = int(input())
        cont = 2
        numeros = []
        if n == 0:
            numeros  = [0]
            print(f'Caso {caso}: {len(numeros)} numero')
            print(*numeros)
            print('')
        elif n == 1:
            numeros = [0, 1]
            print(f'Caso {caso}: {len(numeros)} numeros')
            print(*numeros)
            print('')
        else:
            numeros = [0, 1]
            while numeros.count(n) != n:
                for x in range(cont):
                    numeros.append(cont)
                cont += 1
            print(f'Caso {caso}: {len(numeros)} numeros')
            print(*numeros)
            print('')
        caso += 1
    except EOFError:
        break