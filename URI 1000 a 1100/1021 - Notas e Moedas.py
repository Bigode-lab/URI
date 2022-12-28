#objetivo dado um valor calcular quanto esse valor e dado em notas e moedas
valor = float((input()))
#leitura do valor
a = valor
cem = a//100
resto = a%100
cinq = resto//50
resto = resto%50
vinte = resto//20
resto = resto%20
dez = resto//10
resto = resto%10
cinco = resto//5
resto = resto%5
dois = resto//2
resto = resto%2
um = resto//1
#se enconctra quantas notas de determina cedula se tem no valor e se retira essa quantia do valor
#ate chegar a cedula de 2 real

e = valor*100
b = int(e)

m = b%100
cent50 = m//50
m = m%50
cent25 = m//25
m = m%25
cent10 = m//10
m = m%10
cent5 = m//5
cent1 = m%5
#se enconctra quantas moedas de determinado valor se tem no valor e se retira essa quantia do valor
#ate chegar na moeda de 1 centavo
print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(cem)))
print("{} nota(s) de R$ 50.00".format(int(cinq)))
print("{} nota(s) de R$ 20.00".format(int(vinte)))
print("{} nota(s) de R$ 10.00".format(int(dez)))
print("{} nota(s) de R$ 5.00".format(int(cinco)))
print("{} nota(s) de R$ 2.00".format(int(dois)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(um)))
print("{} moeda(s) de R$ 0.50".format(int(cent50)))
print("{} moeda(s) de R$ 0.25".format(int(cent25)))
print("{} moeda(s) de R$ 0.10".format(int(cent10)))
print("{} moeda(s) de R$ 0.05".format(int(cent5)))
print("{} moeda(s) de R$ 0.01".format(int(cent1)))
