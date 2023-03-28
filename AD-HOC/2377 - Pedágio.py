comprimento, distancia = (int(x) for x in input().split())
custo, pedagio = (int(x) for x in input().split())
pagar = (comprimento*custo) + (pedagio*(comprimento//distancia))
print(pagar)