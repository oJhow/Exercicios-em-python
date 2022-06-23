var: str = str(input('digite qualquer coisa: ')).strip().lower()


print('{} Possui {} letras "A" .'.format(var,var.count('a')))
print('A letra "A" apareceu na primeira vez na posição {}.'.format(var.find('a')+1))
print('a letra "A apareceu pela ultima vez na posição {}.'.format(var.rfind('a')+1))


