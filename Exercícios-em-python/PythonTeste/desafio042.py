r1 = float(input('digite o valor da primeira reta: '))
r2 = float(input('digite o valor da segunda reta: '))
r3 = float(input('digite o valor da terceira reta: '))

print('os valores digitados foram {}, {}, {}'.format(r1,r2,r3))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:

    print ('forma um triangulo.')
    if r1 == r2 and r1 == r3:
        print('Triangulo equilátero.')
    elif r1 == r2 or r1==r3:
        print('triangulo isoceles')
    else:
        print('trianguilo escaleno.')

else:
    print('não é possivel formar um triangulo.')