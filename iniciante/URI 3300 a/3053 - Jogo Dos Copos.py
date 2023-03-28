jogadas = int(input())
atual = input()
for x in range(jogadas):
    jogada = int(input())
    if jogada == 1 and (atual == 'A' or atual =='B'):
        if atual == 'A':
            atual = 'B'
        elif atual == 'B':
            atual ='A'
    elif jogada == 2 and (atual == 'C' or atual =='B'):
        if atual == 'B':
            atual = 'C'
        elif atual == 'C':
            atual ='B'
    elif jogada == 3 and (atual == 'A' or atual =='C'):
        if atual == 'A':
            atual = 'C'
        elif atual == 'C':
            atual ='A'
print(atual)