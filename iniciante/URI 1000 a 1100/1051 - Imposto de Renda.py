#calcular o imposto de renda de uma pessoa
def oito(salario):
    #calcula o impostod e renda de 8 porcento
    salario -= 2000 
    #retirada da parte do salario que e insenta de imposto
    imposto = (8/100)*n
    #calculo da parte do imposto que e de 8 porcento
    print('R$ {:.2f}'.format(imposto))
    #impresao do imposto

def dezoito(salario):
    #calcula o impostod e renda de 18 porcento
    salario -= 2000
    #retirada da parte do salario que e insenta de imposto
    imposto = 1000*(8/100)
    #calculo da parte do imposto que e de 8 porcento
    salario  -= 1000
    #retirada da parte do salario que e o imposto e de 8 porcento
    imposto += n*(18/100)
    #calculo da parte do imposto que e de 18 porcento
    print('R$ {:.2f}'.format(imposto))
    #impressao do valor total do imposto

def vinte(salario):
    #calcula o impostod e renda de 20 porcento
    salario -= 2000
    #retirada da parte do salario que e insenta de imposto
    imposto = 1000*(8/100)
    #calculo da parte do imposto que e de 8 porcento
    salario  -= 1000
    #retirada da parte do salario que e o imposto e de 8 porcento
    imposto += 1500*(18/100)
    #calculo da parte do imposto que e de 18 porcento
    salario -= 1500
    #retirada da parte do salario que e o imposto e de 18 porcento
    imposto += n*(28/100)
    #calculo da parte do imposto que e de 28 porcento
    print('R$ {:.2f}'.format(imposto))
    #impressao do valor total do imposto

salario = float(input())
#leitura do salario
if salario >= 0 and salario <=2000:
    print('Isento')
elif salario >2000 and salario <= 3000:
    oito(salario)
elif salario >3000 and salario <= 4500:
    dezoito(salario)
elif salario > 4500:
    vinte(salario)
#avaliacao de qual caso o salario do individuo se encontra e chamamento da funcao respequitiva 
