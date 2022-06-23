print('soma dos pares')
s = 0
c = 0
for p in range (0,6):
    n = int(input('digite um numero: '))
    if (n % 2) == 0 :
        s += n
        c += 1
print('você informou {} numeros pares e a soma deles é {}'.format(c,s))
