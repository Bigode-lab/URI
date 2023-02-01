#determinar qual combustivel tem a preferência de uso de seus clientes
j = True
#j e uma variavel sentinela
alcool = 0
gasolina = 0
diesel = 0
#inicializacao das variaveis alcool, gasolina e disel 
#que vão ser utilizadas para contar as vezes que cada respectivo combustivel foi escolhido
while j:
    #loop usado para fazer varias leituras de um valor que vai ser qual combustivel foi utilizado
    n = int(input())
    #n recebe um valor inteiro 
    if n == 1:
        alcool += 1
        #se n for 1 entao o combustivel e alcool
        #assim somamos + 1 a alcool
    elif n == 2:
        gasolina+= 1
        #se n for 2 entao o combustivel e gasolina
        #assim somamos + 1 a gasolina
    elif n == 3:
        diesel+= 1
        #se n for 1 entao o combustivel e diesel
        #assim somamos + 1 a diesel
    elif n == 4:
        j = False
        #quando n for 4 j recebe Falso o que significa que e o fim do loop
print('MUITO OBRIGADO')
print('Alcool: {}'.format(a))
print('Gasolina: {}'.format(g))
print('Diesel: {}'.format(d))
#impressao da quantidade de vezes que cada combustivel foi escolhido e seus respectivos nomes