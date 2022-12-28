while True:
    try:
        volume = float(input())
        raio = float(input())/2
        altura = volume/(3.14*(raio**2))
        area = (3.14*(raio**2))
        print('ALTURA = {:.2f}'.format(altura))
        print('AREA = {:.2f}'.format(area))
    except EOFError:
        break 