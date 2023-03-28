pull = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
caso = int(input())
for x in range(caso):
    aux = ''
    cripto = input()
    chave = int(input())
    for x in cripto:
        a = pull.index(x)
        if a - chave < 0:
            z = (a - chave) + 26
            aux += pull[z]
        else:
            z = a - chave
            aux += pull[z]
    print(aux)