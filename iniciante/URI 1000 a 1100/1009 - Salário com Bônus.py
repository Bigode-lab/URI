#calcular o valor do salario de um funcionario junto com a comissao 
vendedor = input()
#letura do nome do vendedor
salario = float(input())
#letura do salario fixo do vendedor
vendas = float(input())
#letura de vendas realizadas pelo vendedor
comissao  = vendas*15/100
#calculo da comissao
recebe = comissao + salario
#salario juntamente com a comissao
print('TOTAL = R$ {:.2f}'.format(recebe))
#impresao do total que o vendedor vai receber
