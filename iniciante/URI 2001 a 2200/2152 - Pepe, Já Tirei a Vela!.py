casos = int(input())
for x in range(casos):
    hora, minuto, ocorrencia = (int(x) for x in input().split())
    if hora < 10:
        hora = '0'+str(hora)
    if minuto < 10:
        minuto = '0'+str(minuto)
    if ocorrencia == 0:
        ocorrencia = 'A porta fechou!'
    else:
        ocorrencia = 'A porta abriu!'
    print(f'{hora}:{minuto} - {ocorrencia}')