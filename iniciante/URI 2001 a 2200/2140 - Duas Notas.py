while True:
    compra, pago = (int(x) for x in input().split()) 
    if  (compra == pago and compra== 0):
        break
    troco = pago - compra
    notas = [2, 5, 10, 20, 50, 100]
    if troco > 200 or troco < 5:
        posibididade = 'impossible'
    elif troco in notas :
        posibididade = 'possible'
    else:
        for cedula in notas:
            if (troco - cedula) >= 2 and  (troco - cedula) in notas:
                posibididade = 'possible'
                break
            else:
                posibididade = 'impossible'
    print(posibididade)