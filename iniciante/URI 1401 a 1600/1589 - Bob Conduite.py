#obejetio retornar o menor raio da soma de duas circunferencias
n = int(input())
#leitura de um numero inteiro 
for x in range(n):
    #enquanto x for menor que n
    r1 , r2 = (int(x) for x in input().split())
    #vamos receber dois numeros inteiros que sera os raios das circunferencias
    print(f'{r1 + r2}')
    #printamos a soma deles