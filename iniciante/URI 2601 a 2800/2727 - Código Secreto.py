while True:
    try:
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        casos = int(input())
        for x in range(casos):
            pontos = [str(y) for y in input().split()]
            n = (len(pontos)-1)*3
            n += len(pontos[-1])
            print(alfabeto[n-1])
    except EOFError:
        break