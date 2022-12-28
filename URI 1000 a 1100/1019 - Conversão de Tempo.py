#converta uma quantidade de segundos na forma hh:mm:ss
segundos = int(input())
#leitura dos segundos
horas = segundos//3600
segundos = segundos - horas*3600
minutos = segundos//60
segundos = segundos - minutos*60
#se faz a divisao para encontrar a unidade respequitiva na quatidade de segundos
#se retira essa quantidade de segundos do total ate chegar na quantidade final de segundos
print('{}:{}:{}'.format(horas, minutos, segundos))
#impressao dos segundos no formato hh:mm:ss