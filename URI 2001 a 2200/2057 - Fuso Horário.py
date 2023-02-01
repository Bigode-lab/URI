#objetivo calcular o horario de cegada de uma viajem 
saida, tempo, fuso = (int(x) for x in input().split())
#leitura do horario de saida, tempo da viajem e fuso horario no local de chegada
resultado = saida + tempo + fuso
#caculo do horario de chegada
if resultado >= 24:
    resultado -= 24
elif resultado < 0:
    resultado += 24
#condicoes de correcao do horario
print(f'{resultado}')
#impressao do resultado
