abas, acoes = (int(x) for x in input().split())
#leitura da quantidade de abas iniciais e a quantidade de acoes que pericles fara
for x in range(acoes):
#enquanto x for menor que acoes
    acao = input()
    #leitura da acao
    if acao == 'fechou':
        abas += 1
        #se acao for fechar somamos 1 a abas
    elif acao == 'clicou':
        abas -= 1
        #se a acao for clicou subitraimos 1 das abas
print(abas)
#impressao da quantidade de abas finais
