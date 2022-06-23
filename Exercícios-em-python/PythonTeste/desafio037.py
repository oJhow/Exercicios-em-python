num = int(input('Digite um numero qualquer: '))
al = int(input('escolha qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal:'))

if al == 1:
    binary = bin(num)

    print('O numero {} convertido em Binario é {}.'.format(num,binary [2:]))
elif al== 2:
    octal = oct(num)
    print('O numero {} convertido em octal é {}.'.format(num, octal [2:] ))
elif al == 3:
    hexa = hex(num)


    print('O numero {} convertido em Hexadecimal é {}'.format(num,hexa [2:]))

else:
    print ('Opção invalida!! escolha entre 1, 2 e 3.')
print('............................................................................')
