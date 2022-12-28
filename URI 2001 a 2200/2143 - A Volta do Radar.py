while True:
    n = int(input())
    if n == 0:
        break
    for x in range(n):
        clientes = int(input())
        if clientes%2 == 1:
            pedidos = ((clientes*2) - 1)
            print(pedidos)
        else:
            pedidos = ((clientes*2) - 2)
            print(pedidos)
    

    