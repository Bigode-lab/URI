renas = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen','Rudolph']
bolas = [int(x) for x in input().split()]
soma  = sum(bolas)
resto = soma%9
print(renas[resto-1])