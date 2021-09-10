n = int(input())
for x in range(n):
    reguas = [int(x) for x in input().split()]
    soma = sum(reguas) - (reguas[0] + reguas[0] - 1)
    print(soma)
