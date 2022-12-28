cabaias = 0
coelhos = 0
sapos = 0
ratos = 0
#inicalizacao das variaveis 
casos = int(input())
#leitua do numero de casos
for x in range(n):
  #enquanto x for menor que casos
    numero, cobaia = (str(y) for y in input().split(' '))
    #leitura do numero e qual cobaia
    cobaias += int(numero)
    #soma se a quantidade de animais 
    if cobaia == 'C':
      #se a cobaia for um coelho
      coelhos += int(numero)
      #coelhos recebe a quantidade de coelhos
    elif cobaia == 'S':
      #se a cobaia for um sapo
      sapos += int(numero)
      #sapos recebe a quantidade de sapo
    elif cobaia == 'R':
      #se a cobaia for um rato
      ratos += int(numero)
      #ratos recebe a quantidade de ratos
pc = (coelhos*100)/cabaias 
#pc recebe a porcentagem de coelho dentro das cobaias
ps = (sapos*100)/cabaias 
#ps recebe a porcentagem de sapos dentro das cobaias
pr = (ratos*100)/cabaias 
#pr recebe a porcentagem de ratos dentro das cobaias
print('Total: {} cobaias'.format(cabaias))
print('Total de coelhos: {}'.format(coelhos))
print('Total de ratos: {}'.format(ratos))
print('Total de sapos: {}'.format(sapos))
print('Percentual de coelhos: {:.2f} %'.format(pc))
print('Percentual de ratos: {:.2f} %'.format(pr))
print('Percentual de sapos: {:.2f} %'.format(ps))
#impressao dos dados