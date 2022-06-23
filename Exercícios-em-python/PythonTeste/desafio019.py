import random

a1 = input('digite o nome do aluno: ')
a2 = input('digite o nome do aluno: ')
a3 = input('digite o nome do aluno: ')
a4 = input('digite o nome do aluno: ')

prof = (a1,a2,a3,a4)


print('O aluno selecinado entre {}, {}, {} e {} foi o: {}'.format(a1,a2,a3,a4,random.choice(prof)))

