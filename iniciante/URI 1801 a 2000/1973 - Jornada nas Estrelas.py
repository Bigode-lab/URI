#objetivo : retornar a quantidade de carneiros nao roubados dos sitios e a quantidade de sitios atacados
#observacao 1 :  o irmao louco vai para i+1 se a quantidade de carneiros em i e impar
#observacao 2 :  o irmao louco vai para i-1 se a quantidade de carneiros em i e par
#logica
#ou seja, ele avança ate encontrar um numero par. porque se o irmao louco rouba um por onde ele passa
#como o irmao louco rouba um carneiro por onde ele passa entao todos os sitios antes do numero par de carneiros
#terao um numero par de carneiros tambem
soma = 0
#iniciando a varaivel soma que vai resultar na quantidade de carneiros roubados
atacadas = 0
#iniciando a variavel atacadas que vaia armazenar a quantidade de fazendas atacadas
zeros = False
#iniciando a variavel zeros que vai funcioanr como uma varaivel sentinela
#para saber se vai ter alguma fazenda que apos o irmao louco passar vai ficar com nenhum carneiro
zero = 0
#quantidade de fazenda que apos o irmao louco passar fico sem carneiros
sitios = int(input())
#leitura da quantidade de sitios contidos na estrada
carneiros = [int(x) for x in input().split()]
#lendo a quantidade de carneiros em cada sitio e armazenando em uma lista
for i in range(sitios):
    #enquanto i for menor que sitios
    #vamos percorrer a lista pelo indice 
    if carneiros[i]%2 == 0:
        #se a quantidade de carneiros no sitio i e par
        soma+=i+1
        #somase i+1 a soma, estamos fazendo a simulacao da soma aqui para nao ter que calculaar cada caso
        #somamos i+1 pos o for inicia i em 0 e como ele rouba um carneiro em cada casa temos que somar i+1 a soma
        atacadas += 1
        #somamos +1 aatacadas
        if zeros:
            #se zeros for verdadeiro, ou seja, se tiver alguma fazenda que nao tem carneiros
            soma = soma - zero
            #soma retiramos a quantidade de sitios que nao tem carneiros da soma simulada anteriormente 
        break
        #utilizamos o break para sairmos do for 
    else:
        #se nao
        soma +=1
        #somamos +1 a soma
        if carneiros[i] == 1:
            #se a quantidade de carneiros no sitio i for 1
            #ou seja, que apos o irmao louco passar nao tera mais carneiros nesse sitio
            zeros = True
            zero +=1
            #zeros recebe True e somamos +1 a zero
        atacadas += 1
        #atacas recebe +1
print(f'{atacadas} {sum(carneiros)-soma}')
#imprimindo os objetivos