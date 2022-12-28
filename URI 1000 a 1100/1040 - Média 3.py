#objetivo calcular a media de uma aluno e avaliar se eles esta aprovado ou reprovado
nota1, nota2, nota3, nota4 = (float(x) for x  in input().split())
#leitura de 4 notas
media = ((nota1*2)+(nota2*3)+(nota3*4)+(nota4*1))/10
#calculo da media de cada nota multiplicada pelo seus pesos e dividida pela soma dos pesos
print("Media: {:.1f}".format(media))
#impresao da nota
if (media>=7.0):
    print("Aluno aprovado.")
#se a media for maior que 7 o aluno esta aprovado
elif (media<5):
    print("Aluno reprovado.")
#se a media for menor que 5 o aluno esta reprovado
elif (5<= media<7):
    print("Aluno em exame.")
    #se estiver entre 5 e 7 ele esta em exame
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    #leitura e impresao da nota do exame do aluno
    media = (media + exame)/2
    #calculando a media novamente
    if (media>=5):
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(media))
    #se a media for maior q 5 ele esta aprovado e impressao da nota
    elif (media<5):
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(media))
    #se a  media for menor que 5 ele esta reprovado e impressao da media final