while True:
    try:
        a = input()
        maiuscula = True
        minuscula = False
        aux = ''
        for x in a:
            if x.isalpha():
                if maiuscula:
                    aux += x.upper()
                    maiuscula = False
                    minuscula = True
                elif minuscula:
                    aux += x.lower()
                    maiuscula = True
                    minuscula = False
            else:
                aux += x
        print(aux)
    except EOFError:
        break