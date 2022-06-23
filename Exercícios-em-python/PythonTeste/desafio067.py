

while True :
    t = int (input('Digite um numero que queira saber a tabuada:'))

    print('-' * 20)

    if t < 0:
        break
    for c in range (0,11):
        a = t*c

        print (f' {t} x {c} = {a}')
    print('-' * 20)

print ('Programa encerrado.')