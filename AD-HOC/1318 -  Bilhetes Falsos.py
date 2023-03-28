originais, presentes = (int(x) for x in input().split())
while originais and presentes != 0:
    bilhetes = [int(x) for x in input().split()]
    ori = []
    falso = 0
    for x in bilhetes:
        if x not in ori:
            ori.append(x)
            if bilhetes.count(x) > 1:
                falso += 1
    print(falso)

    originais, presentes = (int(x) for x in input().split())    