p = int(input('digite um numero: '))
cont = 0
for c  in range (1, p+1):
    if p % c ==0:
        print('\033[32m', end=' ')
        cont +=1
    else:
        print('\33[31m', end=' ')
    print ('{}'.format(c),end = ' ')
print('\n\033[mo numero {} foi dividido {} vezes.'.format(p,cont))
if cont == 2:
    print('devido a isso ele é primo.')
else:
    print('devido a isso ele não é primo.')

