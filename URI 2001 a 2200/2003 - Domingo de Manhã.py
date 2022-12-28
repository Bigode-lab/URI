while True:
    try:
        hora, minutos = (int(x) for x in input().split(':'))
        minutos += hora*60 + 60
        atraso = (8*60) - minutos
        if atraso < 0:
            print(f'Atraso maximo: {abs(atraso)}')
        else:
            print(f'Atraso maximo: {0}')
    except EOFError:
        break