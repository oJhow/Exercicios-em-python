n1 = int(input('Digite um numero inteiro: '))
n2= int(input('digite outro numero inteiro: '))

if n1>n2:
    print('o primeiro valor que é {} é maior que o segundo que é {}'.format(n1,n2))
elif n2>n1:
    print('O segundo valor que é {} é maior que o primeiro que é {}'. format(n2,n1))
else:
    print('não há diferença entre os numeros {} e {}, eles são iguais.'.format(n1,n2))
print('...............')