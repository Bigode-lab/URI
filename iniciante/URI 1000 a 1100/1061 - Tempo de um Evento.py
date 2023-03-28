#objetivo calcular o tempo de duracao de um evento 
d, dias_inicial = (str(x) for x in input().split())
#leitura do dia inicial
horas_iniciais, minutos_iniciais, segundos_iniciais = (int(x) for x in input().split(' : '))
#leitura do horario inicial no formato hh:mm:ss
d, dias_final = (str(x) for x in input().split())
#leitura do dia final
horas_final, minutos_final, segundos_final = (int(x) for x in input().split(' : '))
#leitura do horario final no formato hh:mm:ss
segundos_inicial = (int(dias_inicial)*24*60*60) + (horas_iniciais*60*60) + (minutos_iniciais*60) + segundos_iniciais
#transformando o dia e a hora inicial para segundos
segundos_final = (int(dias_final)*24*60*60) + (horas_final*60*60) + (minutos_final*60) + segundos_final
#transformando o dia e a hora final para segundos
segundos = segundos_final - segundos_inicial
#fazendo a diferenca dos segundos totais inicias e finais para obter o tempo do evento
dias = segundos//(24*60*60)
#fazendo a transformacao para achas quantos dias se passou
segundos = segundos%(24*60*60)
#retirando os segundos dos dias dos segundos totais para calcular as demais unidades
horas = segundos//(60*60)
#fazendo a transformacao para achas quantas horas se passou
segundos = segundos%(60*60)
#retirando os segundos das horas dos segundos totais para calcular as demais unidades
minutos = segundos//(60)
#fazendo a transformacao para achas quantos minutos se passou
segundos = segundos%(60)
#retirando os segundos dos minutos dos segundos totais 
print(f'{dias} dia(s)\n{horas} hora(s)\n{minutos} minuto(s)\n{segundos} segundo(s)')
#impressao do tempo deduracao do evento