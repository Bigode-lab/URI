#iprimir o resultado da soma dos termos de s
casos = int(input())
#leitura de um numero interiro que epresenta a quantidade de testes
for x in range(casos):
    #enquanto x for menor que casos
    termos = int(input())
    #leitura da quantidade de termos de s
    if termos%2 == 0:
        print(0)
        #se termos for um numero par entao a soma da 0
    else:
        #se termos for um numero impar entao a soma e 1
        print(1)