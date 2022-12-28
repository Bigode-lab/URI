n = int(input())
for x in range(n):
    sheldon, raj = (str(s) for s in input().split())
    if raj == sheldon:
        r = 'De novo!'
    #sheldon
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
    #raj
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