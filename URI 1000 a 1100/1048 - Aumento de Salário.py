#objetivo calcular o reajuste e dar o novo salario do funcionario
def quinze(salario):
    #funcao que vai calcular o reajuste de aumento de 15 porcento
    reajuste = salario*(15/100)
    #calculo do reajuste
    salario = salario + reajuste
    #novo salario do funcionario
    percentual = 15
    #percentual do aumento
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(salario, reajuste, percentual))
    #impressao dos dados
    
def doze(salario):
    #funcao que vai calcular o reajuste de aumento de 12 porcento
    reajuste = n*(12/100)
    #calculo do reajuste
    salario = salario + reajuste
    #novo salario do funcionario
    percentual = 12
    #percentual do aumento
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(salario, reajuste, percentual))
    #impressao dos dados

def dez(salario):
    #funcao que vai calcular o reajuste de aumento de 10 porcento
    reajuste = n*(10/100)
    #calculo do reajuste
    salario = salario + reajuste
    #novo salario do funcionario
    percentual = 10
    #percentual do aumento
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(salario, reajuste, percentual))
    #impressao dos dados

def sete(salario):
    #funcao que vai calcular o reajuste de aumento de 7 porcento
    reajuste = n*(7/100)
    #calculo do reajuste
    salario = salario + reajuste
    #novo salario do funcionario
    percentual = 7
    #percentual do aumento
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(salario, reajuste, percentual))
    #impressao dos dados

def quatro(salario):
    #funcao que vai calcular o reajuste de aumento de 4 porcento
    reajuste = n*(4/100)
    #calculo do reajuste
    salario = salario + reajuste
    #novo salario do funcionario
    percentual = 4
    #percentual do aumento
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(salario, reajuste, percentual))
    #impressao dos dados

salario = float(input())
#leitura do salario atual do funcionario

if salario >= 0 and salario <= 400.00:
    quinze(salario)
elif salario >= 400.01 and salario <= 800.00:
    doze(salario)
elif salario >= 800.01 and salario <= 1200.00:
    dez(salario)
elif salario >= 1201.00 and salario <= 2000.00:
    sete(salario)
elif salario > 2000.00:
    quatro(salario)
#condicional de qual caso de reajuste o salario do funcionario se enquadra e chamando a funcao respequitiva 