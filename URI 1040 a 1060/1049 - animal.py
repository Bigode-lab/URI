palavra  = input()
if palavra == 'vertebrado':
    palavra  = input()
    if palavra == 'ave':
        palavra  = input()
        if palavra == 'carnivero':
            print('aguia')
        else:
            print('pomba')
    else:
        palavra  = input()
        if palavra == 'mamifero':
            palavra  = input()
            if palavra == 'onivoro':
                print('homem')
            else:
                print("vaca")
else:
    palavra  = input()
    if palavra == 'inseto':
        palavra  = input()
        if palavra == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        palavra  = input()
        if palavra == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
