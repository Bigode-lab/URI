digito, numero  = (str(x) for x in input().split(' '))
aux = ''
while  digito and numero != '0':
    for x in numero:
        if x == digito:
            continue
        elif x != digito and aux == '' and x == '0':
            continue
        else:
            aux += x
    if aux == '' :
        print('0')
    else:
        print(aux)
    digito, numero  = (str(x) for x in input().split(' '))
    aux = ''