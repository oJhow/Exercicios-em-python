from datetime import date
from time import sleep
atual = date.today().year
print('CATEGORIA ESPORTIVA DE NATAÇÃO.')

nac = int(input('Digite o ano de nascimento:'))

id = atual - nac

print('ANALISANDO...')

sleep(2)

print('você tem {} anos.'.format(id))

if id <= 9:
    print('\033[0:32mcategoria até 9 anos.')
    print('você pertence a categoria mirim.')
elif id > 9 and id <=14:
    print('\033[0:32mCategoria até 14 anos.')
    print('você pertence a categoria infantil.')
elif id > 14 and id <= 19:
    print('\033[0:32mcategoria até 19 anos.')
    print('você pertence a categoria junior.')
elif id > 19 and id <= 25:
    print('\033[0:32mcategoria até 25 anos.')
    print('você pertence a categoria senior.')
else:
    print('\033[0:32mcategoria acima de 25 anos.')
    print('você pertence a categoria master.')
print('Boa sorte!')


