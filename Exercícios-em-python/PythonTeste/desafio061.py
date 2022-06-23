print ('calculo de Progressão aritmética')
p = int (input('digite o primeiro termo: '))
r = int (input('digite a razão da PA: '))
termo = p
cont = 1

while cont <= 10:
    print ('{} > '.format (termo),end='')
    termo += r
    cont +=1


print ('fim')
