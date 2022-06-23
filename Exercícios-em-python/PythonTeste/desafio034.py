sal = float(input('digite o seu salário em R$: '))


print('o salário digitado foi de {} R$.'.format(sal))
if sal > 1250.00:

    print('o seu aumento é de 10%')
    print ('seu novo salário é {:.2f} R$'.format((sal*0.10)+sal))
else:
    print(' o seu aumento é de 15%')
    print('seu novo salário é {:.2f} R$'.format((sal*0.15)+sal))

