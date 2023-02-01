#objetivo retornar a divisao inteira entre dois numeros inteiros e o resto da diisao
a, b = (int(x) for x in input().split())
#leitura de dois numeros inteiros
if b < 0:
    #se b for menor que 0
    print(f'{(a//-b)*-1} {a%-b}')
    #impressao da divisao so que multiplicando b por -
else:
    print(f'{a//b} {a%b}')
    #impressao da divisao de forma normal