def p(l):
    for x in range(len(l)):
        print('par[{}] = {}'.format(x, l[x]))
    
def im(l):
    for x in range(len(l)):
        print('impar[{}] = {}'.format(x, l[x]))
        
        
par = []
impar = []
for x in range(15):
    n = int(input())
    a = n%2
    if a == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        p(par)
        par = []
    elif len(impar) == 5:
        im(impar)
        impar = []
if len(impar) > 0:
    im(impar)
if len(par) > 0:
    p(par)