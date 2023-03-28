contador = 0
mensagem = input()
for x in mensagem:
    if x == '1':
        contador += 1
if contador%2 == 0:
    mensagem += '0'
else:
    mensagem += '1'
print(mensagem)