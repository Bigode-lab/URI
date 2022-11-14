def fibonacci(n):
    global contador
    contador +=1
    if n == 0 and contador == 1:
        return []

    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    else:
        ant = fibonacci(n - 1)
        return ant + [ant[-2] + ant[-1]]

contador = 0
n = int(input())
print(*fibonacci(n))