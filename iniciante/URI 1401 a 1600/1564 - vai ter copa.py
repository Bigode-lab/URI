#objetivo imprimir a resposta da presidente
#utiliacao de um laco pois o fim do arquivo contem um eof
while True:
    try:
        reclamacoes = int(input())
        #leitura de um avaor inteiro representando a quantidade de reclamacoes
        if reclamacoes == 0:
            print('vai ter copa!')
            #se reclamacoes for igual a ero ela reponda vai ter copa
        else:
            print('vai ter duas!')
            #se tiver recamacoes ela responde vai ter duas
    except EOFError:
        #se ler um EOF
        break
        #se tem a saida do loop e o fim do programa