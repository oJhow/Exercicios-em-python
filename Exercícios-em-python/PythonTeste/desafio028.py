import random
from time import sleep

print(' tente adivinhar o numero que o computador pensou entre 0 e 5.')

adv = int(input('digite um numero entre 0 e 5: '))

r = random.randint(0,5)

print ('o numero que o computador pensou foi {}.'.format(r))

print ('PROCESSANDO...')
sleep(3)
if adv == r:

    print('parabens você ganhou')
else:
    print('você perdeu')