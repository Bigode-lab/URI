jips = 0
turistas = 0
while True:
    estado = [str(x) for x in input().split()]
    if estado[0] == 'SALIDA':
        jips += 1
        turistas += int(estado[1])
    elif estado[0] == 'VUELTA':
        jips -= 1
        turistas -= int(estado[1])
    elif estado[0] == 'ABEND':
        break
print(turistas)
print(jips)