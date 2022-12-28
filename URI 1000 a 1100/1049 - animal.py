#objetivo descobrir qual qnimal e por uma quantidade de caracteristicas 
a = input()
b = input()
c = input()
#leitura do nome de tres caracteristicas do tipo de um animal

if a == 'vertebrado' and b == 'ave' and c == 'carnivoro':
    animal = 'aguia'
if a == 'vertebrado' and b == 'ave' and c == 'onivoro':
    animal = 'pomba'
if a == 'vertebrado' and b == 'mamifero'   and c == 'onivoro':
    animal = 'homem'
if a == 'vertebrado' and b == 'mamifero' and c == 'herbivoro':
    animal = 'vaca'
if a == 'invertebrado' and b == 'inseto' and c == 'herbivoro':
    animal = 'lagarta'
if a == 'invertebrado' and b == 'inseto' and c == 'hematofago':
    animal = 'pulga'
if a == 'invertebrado' and b == 'anelideo' and c == 'onivoro':
    animal = 'minhoca'
if a == 'invertebrado' and b == 'anelideo' and c == 'hematofago':
    animal = 'sanguessuga'
#avaliacao de casos e fazendo a identificacao do animal
print(animal)
#impresao do animal 