#objetivo imprimir a saida da sequencia criada de com o final de um numero
#a sequencia e formada repetido um numero n n vezes na sequencia 
caso = 1
#iniciando a variavel caso
while True:
#como o fim do arquivo e com um EOF utilizamos um laço while sempre verdadeiro que tera saida quando entrar o EOF
    try:
        numero = int(input())
        #leitura de um numero que sera o ultimo numero da sequencia
        repeticoes = 2
        #iniciando a variael contador em 2
        #pos o numero dois e o primeiro numero que aparece mais de uma ve na sequencia
        #utilizaremos essa vvariavel para contar a quantidade de vezes que um numero n se repete
        #apartir do 2
        if numero == 0:
            numeros  = [0]
            print(f'Caso {caso}: {len(numeros)} numero')
            print(*numeros)
            print('')
	#se numero for igual a zero a sequencia tera apenas o numero 0 
	#entao imprimimos a sequencia apenas com o zero e o caso
	#e imprimos uma quebra de linha para a saida ficar igual a pedida
        elif n == 1:
            numeros = [0, 1]
            print(f'Caso {caso}: {len(numeros)} numeros')
            print(*numeros)
            print('')
        #se numero for igual a um a sequencia tera apenas o numero 0, q
	#entao imprimimos a sequencia apenas com o zero um e o caso
	#e imprimos uma quebra de linha para a saida ficar igual a pedida
        else:
            numeros = [0, 1]
            #iniciamos a lista com os dois numeros que se repetem apenas uma vez
            while numeros.count(numero) != numero:
            #enquanto a quantidade de vezes que o numero aparecer na lista
            #for diferente de n 
                for x in range(cont):
                    numeros.append(cont)
                #enquanto x for menor que cont adicionaremos o cont a lista 
                #ou seja, adicionaremos n vezes um numero n para se formar a sequencia
                #ate cegarmos na sequencia que queremos que seja formada
                cont += 1
               	#somamos 1 no cont  para ir que comecemos a implementar o proximo n
               	#ate cegarmos ao numero
            print(f'Caso {caso}: {len(numeros)} numeros')
            print(*numeros)
            print('')
            #impressao da sequencia e o caso e a quebra de lina formando a saida pedida
        caso += 1
        #somamos 1 na variael caso
    except EOFError:
        break
