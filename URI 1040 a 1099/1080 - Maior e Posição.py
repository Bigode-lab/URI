for x in range(100):
    n = int(input())
    if x == 0:
        maior = n
        posição = x + 1
    if n > maior:
        maior = n
        posiçao = x + 1 
print(maior)
print(posiçao)