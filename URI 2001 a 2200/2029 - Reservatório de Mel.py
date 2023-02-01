#objetivo calcular a altura e a area de um reservatorio de mel
while True:
    try:
        volume = float(input())
        #leitura do volume 
        raio = float(input())/2
        #leitura do raio, ele da o diametro mas na leitura ja estamos fazendo a divisao por 2 
        #obtendo o raio
        altura = volume/(3.14*(raio**2))
        #calculo da altura do reservatorio de meu
        area = (3.14*(raio**2))
        #calcuo da area do reservatorio de meu
        print('ALTURA = {:.2f}'.format(altura))
        print('AREA = {:.2f}'.format(area))
        #impressao da altira e da area do reservatorio de mel
    except EOFError:
        break 
