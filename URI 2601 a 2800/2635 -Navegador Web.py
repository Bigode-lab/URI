def buscadas(palavra, pesquisadas):
    #funcao feita para calcular as ocorrencias de busca da palavra em pesquisadas
    maior = 0
    ocorrencia = 0
    #iniciando duas variaveis uma que armazenara a 
    for x in pesquisadas:
        #percorrendo as palavra em pesquisadas
        if x[0:len(palavra)] == palavra:
            #se o comeco da palavra x for igual a palvra que esta sendo buscada
            ocorrencia +=1
            #somamos mais um a ocorrencia
            if len(x) > maior:
                maior = len(x)
                #quando o tamanho de x for maio do que o tamaio da maior palavra antes esquisada
                #maior recebe o tamanho de x 
    if ocorrencia == 0:
        return -1, 0
        #se ocorrencia for 0 retornamos -1, 0
    else:
        return ocorrencia, maior
        #se nao retornamos ocorrencia e o tamanho da maior palavra
        
buscada = int(input())
#numero de palavras buscadas
pesquisadas = []
#inicializando a lista pesquisadas que armazenara as palavras pesquisadas
for x in range(buscada):
    #enquanto x for menor que buscada
    palavra = input()
    #leitura da palavra buscada
    pesquisadas.append(palavra)
    #armazenando ela nas palavras pesquisadas
buscar = int(input())
#leitura do numero de palavras que serao buscadas
for x in range(buscar):
    #enquanto x for menor que buscar
    palavra = input()
    #leitura da paavra
    ocorrencia, maior = buscadas(palavra, pesquisadas)
    #chamada da funcao buscadas que retornara o numero de palavras
    #que aparecem no historico de busca e o tamanho da maior
    if maior == 0:
        print(-1)
        #se maior for igual a 0 impresao do -1 pois nao existe ocorrencia
    else:
        print(ocorrencia, maior)
        #se nao impressao das ocorrencias e o tamanho da maior 
    