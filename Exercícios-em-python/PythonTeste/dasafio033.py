n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
n3 = int(input('digite o terceiro numero:'))
maior = n1

print ('os numeros digitados foram {}, {} e {}.'.format(n1,n2,n3))



if (n2 > maior):
    maior = n2

if (n3 > maior):
    maior = n3
print('o maior numero é {}'.format(maior))

menor = n1

if (n2 < menor):
    menor = n2

if (n3 < menor):
    menor = n3
print('o menor numero é {}.'. format(menor))


