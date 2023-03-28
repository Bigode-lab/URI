#dizer o resultado do jogo
repeticoes = int(input())
#leitura de um inteiro que e a quantidade de repeticoes 
for x in range(repeticoes):
    #enquano x for menor que repeticoes
    sheldon, raj = (str(s) for s in input().split())
    #eitura das jogadas de sheldon e raj
    if raj == sheldon:
        r = 'De novo!'
    #se ees jogarem a mesma coisa jogam de novo
    # casos em q sheldon ganha
    elif (sheldon == 'tesoura') and (raj == 'papel' or raj == 'lagarto'):
        r = 'Bazinga!'
    elif (sheldon == 'papel') and (raj == 'pedra' or raj == 'Spock'):
        r = 'Bazinga!'
    elif (sheldon == 'pedra') and (raj == 'tesoura' or raj == 'lagarto'):
        r = 'Bazinga!'
    elif (sheldon == 'lagarto') and (raj == 'papel' or raj == 'Spock'):
        r = 'Bazinga!'
    elif (sheldon == 'Spock') and (raj == 'tesoura' or raj == 'pedra'):
        r = 'Bazinga!'
    #casos em que raj ganha
    elif (raj == 'tesoura') and (sheldon == 'papel' or sheldon == 'lagarto'):
        r = 'Raj trapaceou!'
    elif (raj == 'papel') and (sheldon == 'pedra' or sheldon == 'Spock'):
        r = 'Raj trapaceou!'
    elif (raj == 'pedra') and (sheldon == 'tesoura' or sheldon == 'lagarto'):
        r = 'Raj trapaceou!'
    elif (raj == 'lagarto') and (sheldon == 'papel' or sheldon == 'Spock'):
        r = 'Raj trapaceou!'
    elif (raj == 'Spock') and (sheldon == 'tesoura' or sheldon == 'pedra'):
        r = 'Raj trapaceou!'
    print(f'Caso #{x + 1}: {r}')
    #impresao do caso e da resposta de quem ganhou 