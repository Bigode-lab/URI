#objetivo calcular o valor a ser pago pela compra de duas pecas 
codigo1, numero1, valor1 = (float(x) for x in input().split())
#leitura do codigo da primeira peca, leitura do numero de pecas da primeira peca
#leitura do valor de cada unidade da primeira peca
codigo2, numero2, valor2 = (float(x) for x in input().split())
#leitura do codigo da segunda peca, leitura do numero de pecas da segunda peca
#leitura do valor de cada unidade da segunda peca
pagar  = (numero1*valor1) + (numero2*valor2)
#calculo do valor a ser pago
print('VALOR A PAGAR: R$ {:.2f}'.format(pagar))
#impressao do valor a ser pago com limitacao de 2 casas decimais