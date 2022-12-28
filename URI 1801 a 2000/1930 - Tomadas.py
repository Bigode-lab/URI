def calcularTomadasLivres(reguas):
    totalReguas = len(reguas)
    
    tomadasTotal = 0
    for regua in reguas:
        tomadasTotal += regua
    
    tomadasRestantes = tomadasTotal - (totalReguas - 1)
    
    print(tomadasRestantes)

entrada = [int(x) for x in input().split()]
calcularTomadasLivres(entrada)