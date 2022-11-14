def quinze(n):
    reajuste = n*(15/100)
    n = n + reajuste
    percentual = 15
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(n, reajuste, percentual))
def doze(n):
    reajuste = n*(12/100)
    n = n + reajuste
    percentual = 12
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(n, reajuste, percentual))

def dez(n):
    reajuste = n*(10/100)
    n = n + reajuste
    percentual = 10
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(n, reajuste, percentual))

def sete(n):
    reajuste = n*(7/100)
    n = n + reajuste
    percentual = 7
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(n, reajuste, percentual))

def quatro(n):
    reajuste = n*(4/100)
    n = n + reajuste
    percentual = 4
    print('Novo salario: {:.2f}\nReajuste ganho: {:.2f}\nEm percentual: {:} %'.format(n, reajuste, percentual))

n = float(input())

if n >= 0 and n<= 400.00:
    quinze(n)
elif n >= 400.01 and n<= 800.00:
    doze(n)
elif n >= 800.01 and n<= 1200.00:
    dez(n)
elif n >= 1201.00 and n<= 2000.00:
    sete(n)
elif n > 2000.00:
    quatro(n)