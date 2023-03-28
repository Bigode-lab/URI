#objetivo trasformar a idade dade em anos, meses e dias
idade = int(input())
#leitura da idade em dias
ano = idade//365
idade = idade - ano*365
#descobrindo quantos anos se tem e retirando do total de da idade inicial
mes = idade//30
idade = idade - mes*30
#descobrindo quantos meses se tem e retirando do total de da idade inicial
dia = idade//1
#descobrindo quantos dias se tem 
print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))
#impresao dos dias, meses e anos