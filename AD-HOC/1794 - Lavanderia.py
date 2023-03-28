roupas = int(input())
la,  lb = (int(x) for x in input().split())
sa, sb = (int(x) for x in input().split())
if (roupas >= la and roupas <= lb) and (roupas >= sa and roupas <= sb):
    print('possivel')
else:
    print('impossivel')