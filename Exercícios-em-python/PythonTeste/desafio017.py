from math import hypot

co = float(input('digite o valor do cateto oposto:'))
ca = float(input('digite o calor do cateto adjascente:'))

hp = hypot(co,ca)

print ('o comprimento da hipotenusa com base na soma dos catetos {:.2f} e {:.2f} é ígual a:{:.2f}.'.format(co,ca,hp))
