dentro = 0
fora = 0
#inicializacao das variaveis
casos = int(input())
#numerod e casos de teste
for x in range(casos):
    #enquanto x for menor que casos
    num = int(input())
    #leitura de um numero
    if num >= 10 and num <= 20:
        #se o numero for maior igual a 10 e menor igual a 20
        dentro += 1
        #e somado +1 a variavel dentro, pois o numero esta dentro do intervalo
    else:
        #se nao
        fora += 1
        #e somado +1 a variavel fora, pois o numero esta fora do intervalo
print('{} in'.format(den))
print('{} out'.format(out))
#impressao da quantidade de numeros dentro e fora do intervalo