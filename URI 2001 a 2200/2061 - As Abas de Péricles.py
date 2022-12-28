abas, acoes = (int(x) for x in input().split())
for x in range(acoes):
    acao = input()
    if acao == 'fechou':
        abas += 1
    elif acao == 'clicou':
        abas -= 1
print(abas)