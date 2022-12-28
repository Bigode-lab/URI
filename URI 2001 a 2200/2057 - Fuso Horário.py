saida, tempo, fuso = (int(x) for x in input().split())
resultado = saida + tempo + fuso
if resultado >= 24:
    resultado -= 24
elif resultado < 0:
    resultado += 24
print(f'{resultado}')