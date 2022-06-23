import random

r = random.randint(0,10)



acertou = False
palpites = 0

while not acertou:
    palpites += 1
    adv =int(input('Tente adivinhar o numero que o computador digitou: '))
    if adv == r:
        acertou = True
    else:
        if adv < r:
            print ('Mais....')
        elif adv > r:
            print('Menos....')
print('parabens, você acertou em {} tentativas.'.format(palpites))
print ('o numero que o computador pensou foi {}'.format(r))