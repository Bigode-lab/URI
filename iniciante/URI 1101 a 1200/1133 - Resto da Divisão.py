#obejetivo ler 2 valores a e b e que imprima todos os valores entre eles
#cujo resto da divisão dele por 5 for igual a 2 ou igual a 3
a = int(input())
b = int(input())
#leitura de dois valores a e b
menor = min(a, b)
maior = max(b, a)
#identificando o amior e o menor entre a e b
while menor < maior:
    #enquanto menor for menor que maior
    menor += 1
    #somamos +1 a menor
    #fazemos essa operacao de inicio pq a e b nao estao no intervalo 
    if menor < maior:
        resto = menor%5
        #resto recebe o resto da divisaod e menor por 5
        if resto == 2 or resto == 3:
            print(menor)
            #se o resto for 3 ou 2 imprimos o valor que e menor 