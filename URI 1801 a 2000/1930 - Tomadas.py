#Objetivo calcular o maximo de aparelos que podems ser conectados
def calcularTomadasLivres(reguas):
    totalReguas = len(reguas)
    #calculando quantas reguas se tem
    
    tomadasTotal = 0
    #iniciando a variavel que vai gerar a quantidade de tomadas
    for regua in reguas:
    #percorendo a lista que tem a quantidade de tomadas em cada regua
        tomadasTotal += regua
        #somando a quantidade de tomadas
    
    tomadasRestantes = tomadasTotal - (totalReguas - 1)
    #calculando o maximo de aparelhos que se podem coectar
    
    print(tomadasRestantes)
    #impresao da quantidade maxima de aparelosque podem ser ligados

entrada = [int(x) for x in input().split()]
#leitura da quantidade de tomadas em cada regua
calcularTomadasLivres(entrada)
#funcao que calculara a quantidade de aparelhos que seram conectados
