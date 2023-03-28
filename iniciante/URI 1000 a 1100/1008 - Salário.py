#calcular o salario de um funcionario dado o valor que ele recebe por hora e as horas trabalhadas
numero = int(input())
#leitura do seu numero
horas = int(input())
#leitua da quantidade de horas trabalhadas
valor = float(input())
#leitura do valor de cada hora que o funcionario trabalha
salario = horas * valor
#calculo do salario
print(f'NUMBER = {numero}')
print('SALARY = U$ {:.2f}'.format(salario))
#impressao do salario e do numero do funcionario