from time import sleep
print('Calculando o fatorial.')
f = int(input('Digite um numero que deseja calcular o fatorial: '))

r = 1
c = f
print ('calculando {}! = '.format(f),end='')
sleep(2)
while c > 0:
    print('{}'.format (c), end='')
    print('x' if c > 1 else '=', end='')
    r *= c
    c-=1
print('{}'.format (r),end='')

