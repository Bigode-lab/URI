submissoes = int(input())
while submissoes != 0:
    atual = ''
    acertadas = 0
    tempo_final = 0
    for x in range(submissoes):
        #a = input()
        #print(type(a))
        caso, tempo, julgamento = (str(x) for x in input().split(' '))
        #print(caso)
        if atual != caso:
            atual = caso
            aux = 0
            c = False
        if caso == atual and julgamento == 'incorrect':
            aux += 20
        elif caso == atual and julgamento == 'correct' and c == False:
            acertadas += 1
            tempo_final += aux + int(tempo)
            c = True
    print(f'{acertadas} {tempo_final}')
    submissoes = int(input())