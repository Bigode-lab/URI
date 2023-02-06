#obejetivo retornar se e possivel retornar o troco em duas notas
while True:
    compra, pago = (int(x) for x in input().split()) 
    #leitura do vvalor da compra e do valor pago
    if  (compra == pago and compra== 0):
    #caso em que nao se tem q retornar troco
    #saida do programa
        break
    troco = pago - compra
    #calculo do troco
    notas = [2, 5, 10, 20, 50, 100]
    #uma lista contendo o valor das cedulas inteiras
    if troco > 200 or troco < 5:
        posibididade = 'impossible'
        #se o troco for maior ou menor que o valor de combinacao de cedulas
        #nao e possivel retornar o troco com duas ceduas
    elif troco in notas :
        posibididade = 'possible'
        #se o valor do troco estiver dentro dos valores das cedulas inteiras 
        #e possivel calcular o troco
    else:
        for cedula in notas:
        #percorrendo a lista contenco as notas
            if (troco - cedula) >= 2 and  (troco - cedula) in notas:
            #se o resultado do troco menos a cedula atua for maior do que 2 e tiver mas uma cedula com o valor do troco o troco e possivel
                posibididade = 'possible'
                break
                #saida do for 
            else:
                posibididade = 'impossible'
                #se nao troco nao e possivel
    print(posibididade)
    #imprimindo se e possivel ou nao dar o troco em duas cedulas
