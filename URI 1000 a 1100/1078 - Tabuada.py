#mostrar a tabuada de um numero
indice = 1
#inializacao do numero que vai ficar variando ate 10
#ele vai ser o multiplicador do numero para assim fazer a sua tabuada
numero = int(input())
#leitura de um numero inteiro
while indice<=10:
    #enquanto indice dor menor igual a 10
    print('{} x {} = {}'.format(indice, numero, indice*numero))
    #impressao da operacao deste indice com o numero
    indice += 1
    #indice recebe +1