def função(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1/6
    else:
        return 1/(6 + função(n-1))


repeticoes = int(input())   
if repeticoes == 0:
    repeticoes = 3 
else:
    repeticoes = 3 + (função(repeticoes))

print('{:.10f}'.format(repeticoes)) 