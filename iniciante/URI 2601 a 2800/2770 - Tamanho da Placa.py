while True:
    try:
        h, b, m = (int(x) for x in input().split())
        tamanho = h*b
        for x in range(m):
            d1, d2 = (int(x) for x in input().split())
            if d1*d2 > tamanho:
                print('Nao')
            else:
                print('Sim')
    except EOFError():
        break