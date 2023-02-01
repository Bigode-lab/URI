while True:
    try:
        hora, minutos = (int(x) for x in input().split(':'))
        #leitura da hora e armazenando em minutos e hora
        minutos += hora*60 + 60
        #calculando a quantidade de minutos totais
        atraso = (8*60) - minutos
        #calculando o atraso maximo
        if atraso < 0:
            print(f'Atraso maximo: {abs(atraso)}')
        else:
            print(f'Atraso maximo: {0}')
         #imprimindo o valor do atraso em mminutos
    except EOFError:
        break 
