#imprimir 3 numeros em ordem crescente e em seguida na ordem de entrada
numeros = [int(x) for x in input().split()]
#leitura de uma lista contendo 3 numeros
origenal = numeros.copy()
#armazenano a lista de maneira original
numeros.sort()
#odenacao da lista de maneira crescente 
for x in numeros:
    print(x)
#percoreendoe e imprimindo cada item da lista ordenada
print()
for y in origenal:
    print(y)
##percoreendoe e imprimindo cada item da lista original