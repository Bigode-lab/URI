n = int(input())
for x in range(n):
    alunos, numero = (int(x) for x in input().split())
    respostas = [int(x) for x in input().split()]
    diferenca = []
    for x in respostas:
        diferenca.append(abs(x - numero))
    a = min(diferenca)
    print(diferenca.index(a)+1)