import random
a = input('primeiro aluno: ')
b = input('segundo aluno: ')
c = input('terceiro aluno: ')
d = input('quarto aluno: ')

lista = [a, b, c, d]

random.shuffle(lista)



print (' a ordem de apresentação será:')

print(lista)
