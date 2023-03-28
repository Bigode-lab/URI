#objetivo calcular o menor numero de notas
valor = int(input())
#leitura do valor
original = valor 
#armazenando o valor inicial na variavel original
cem = valor//100 
valor = valor - cem*100 
cinq = valor//50 
valor = valor - cinq*50 
vinte = valor//20 
valor = valor - vinte*20 
dez = valor//10 
valor = valor - dez*100 
cinco = valor//5 
valor = valor - cinco*5 
dois = valor//2 
valor = valor - dois*2 
um = valor//1 
#calculase a quantidade de cedulas da nota maior para a menor em uma divisao inteira
#depois se retira esse valor do total e repetimos os passos ate chegarmos a cedula de 1 real
print("{}".format(original)) 
print("{} nota(s) de R$ 100,00".format(cem))
print("{} nota(s) de R$ 50,00".format(cinq))
print("{} nota(s) de R$ 20,00".format(vinte))
print("{} nota(s) de R$ 10,00".format(dez))
print("{} nota(s) de R$ 5,00".format(cinco))
print("{} nota(s) de R$ 2,00".format(dois))
print("{} nota(s) de R$ 1,00".format(um))
#impressao do valor inicial e quantidade de notas de cada cedula 
