caso = int(input())
for x in range(caso):
    palavra = input()
    aux = ''
    for x in palavra:
        if x.isalpha():
            aux += chr(ord(x) + 3)
        else:
            aux += x
    palavra = aux[::-1]
    aux = ''
    for x in range(len(palavra)//2):
        aux += palavra[x]
    
    for x in range(len(palavra)//2, len(palavra)):
        aux += chr(ord(palavra[x]) -1)
    
    print(aux)