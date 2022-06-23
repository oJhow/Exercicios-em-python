r1 = float(input('digite o valor da primeira reta: '))
r2 = float(input('digite o valor da segunda reta: '))
r3 = float(input('digite o valor da terceira reta: '))

print('os valores digitados foram {}, {}, {}'.format(r1,r2,r3))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:

    print ('forma um triangulo.')
else:
    print('não é possivel formar um triangulo.')