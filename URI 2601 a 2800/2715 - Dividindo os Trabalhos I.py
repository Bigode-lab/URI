#deu erro

while True:
    try:
        elementos = int(input())
        trabalho = [int(x) for x in input().split()]
        j = True
        while len(trabalho) != 0:
            if len(trabalho) == 1 and j:
                print(trabalho[0])
            elif len(trabalho) > 1 and j:
                rangel = trabalho[0]
                trabalho.pop(0)
                gugu = trabalho[-1]
                trabalho.pop()
                j = False
            elif len(trabalho) == 1:
                a = abs((rangel+trabalho[0])-gugu)
                b = abs((trabalho[0]+gugu) - rangel)
                trabalho.pop()
                if a > b:
                    print(b)
                elif a < b:
                    print(a)
                else:
                    print(a)
            elif gugu > rangel:
                rangel += trabalho[0]
                trabalho.pop(0)
            elif gugu < rangel:
                gugu += trabalho[-1]
                trabalho.pop()
            elif rangel == gugu:
                rangel += trabalho[0]
    except EOFError():
        break