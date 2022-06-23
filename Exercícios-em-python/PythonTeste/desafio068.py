import random
print('-'*30)
print('Jogando par ou impar contra o computador.')
print('-'*30)
cont = 0
while True:
    n = int (input('Digite um numero:'))
    c =  (random.randint(0,11))
    r = c + n
    p = ' '
    while p not in 'PI':
        p = str (input('Par ou impar [P/I] ? '))[0].upper().strip()
    print(f'Você jogou {n} e o computador jogou {c} e o total foi {r}.')
    if r % 2 == 0:
        resultado = 'P'
        print (' O resultado foi Par.')
    else:
        resultado = 'I'
        print (' O resultado foi impar.')

    if p != resultado:
        break
    cont += 1
print(f'você perdeu, porem você conseguiu ganhar {cont} vezes conssecutivas')
