def oito(n):
    n -= 2000
    imposto = (8/100)*n
    print('R$ {:.2f}'.format(imposto))

def dezoito(n):
    n -= 2000
    imposto = 1000*(8/100)
    n  -= 1000
    imposto += n*(18/100)
    print('R$ {:.2f}'.format(imposto))

def vinte(n):
    n -= 2000
    imposto = 1000*(8/100)
    n  -= 1000
    imposto += 1500*(18/100)
    n -= 1500
    imposto += n*(24520.008/100)
    
    print('R$ {:.2f}'.format(imposto))

n = float(input())
print(n)
if n >= 0 and n <=2000:
    print('Isento')
elif n>2000 and n <= 3000:
    oito(n)
elif n>3000 and n <= 4500:
    dezoito(n)
elif n > 4500:
    vinte(n)
