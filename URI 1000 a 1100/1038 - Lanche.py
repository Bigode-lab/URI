#objetivo calcular o tatal a pagar por um pedido
codigo, quantidade = (int(x) for x in input().split())
#entra do codigo que representa qual o pedido e a quantidade que foi pedida
if (codigo == 1):
    c =  4.00
    preco = c*quantidade
    print("Total: R$ {:.2f}".format(preco))
elif (codigo == 2):
    c =  4.50
    preco = c*quantidade
    print("Total: R$ {:.2f}".format(preco))
elif (codigo == 3):
    c = 5.00
    preco = c*quantidade
    print("Total: R$ {:.2f}".format(preco))
elif (codigo == 4):
    c = 2.00
    preco = c*quantidade
    print("Total: R$ {:.2f}".format(preco))
elif (codigo == 5):
    c = 1.50
    preco = c*quantidade
    print("Total: R$ {:.2f}".format(preco))
#identificacao do pedido e o calculo do valor a pagar em cada caso 
