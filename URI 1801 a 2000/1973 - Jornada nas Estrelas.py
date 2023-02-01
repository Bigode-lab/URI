#nao esta rodando ainda
estrelas = int(input())
carneiros = [int(x) for x in input().split()]
#roubados = 0
passou = []
estrela = 0
j = True
while j:
    if estrela in range(estrelas):
        #print(f'estrela = {estrela}')
        r = carneiros[estrela]%2
        #print(f'r = {r}')
        #print(f'carneiros = {carneiros[estrela]}')
        if carneiros[estrela] > 0:
            carneiros[estrela] = carneiros[estrela] - 1
            #print(f'carneiros = {carneiros[estrela]}')
        if estrela not in passou:
            passou.append(estrela)
            print(*passou)
        
        if r == 1:
            estrela += 1
            #print(f'estrela = {estrela}')
        else:
            if estrelas >= 0:
                estrela -=1
                #print(f'estrela = {estrela}')
            else:
                j = False
    else:
        j = False

print(f'{len(passou)} {sum(carneiros)}')
            
            
    
