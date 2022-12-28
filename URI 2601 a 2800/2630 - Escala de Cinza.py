def maximo(pixels):
    return max(pixels)
def minimo(pixels):
    return min(pixels)
def mean(pixels):
    return sum(pixels)/len(pixels)
def eye(pixels):
    olho = ((0.30*pixels[0]) + (0.59*pixels[1]) + (0.11*pixels[2]))
    return olho

casos = int(input())
for x in range(casos):
    tipo = input()
    pixel = [int(x) for x in input().split()]
    if tipo == 'min':
        nivel = minimo(pixel)
    elif tipo == 'max':
        nivel = maximo(pixel)
    elif tipo == 'mean':
        nivel = mean(pixel)
    elif tipo == 'eye':
        nivel = eye(pixel)
    print(f'Caso #{x+1}: {int(nivel)}')