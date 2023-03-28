e, f, c = input().split()
soma = int(e) + int(f)
c = int(c)
resultado = 0
while soma >= c:
    novo = soma//c
    garrafa = soma%c
    resultado += novo
    soma = novo + garrafa
print(resultado)