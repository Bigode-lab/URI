def função(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1/2
    else:
        return 1/(2 + função(n-1))


repeticoes = int(input())   
if repeticoes == 0:
    repeticoes = 1 
else:
    repeticoes = 1 + (função(repeticoes))

print('{:.10f}'.format(repeticoes)) 