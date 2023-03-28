#objetivor etornar o maior valor de 3 valores
numeros = [int(x) for x in input().split()]
#lendo e armazenando os 3 valores em uma lista
maior  = max(numeros)
#a funcao max retorna o maior valor da lista que contem os 3 numeros
print(f'{maior} eh o maior')
#impressao do maior valor