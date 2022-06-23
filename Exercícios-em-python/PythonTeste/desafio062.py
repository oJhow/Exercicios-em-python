print ('calculo de Progressão aritmética')
p = int (input('digite o primeiro termo: '))
r = int (input('digite a razão da PA: '))
termo = p
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total+mais
    while cont <= total:
        print ('{} > '.format (termo),end='')
        termo += r
        cont +=1


    print ('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais ? '))
print('a PA gerou {} termos no total.'.format(total))