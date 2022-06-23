from math import sin, cos, tan, radians

ang = float(input('digite um angulo qualquer:'))

seno = sin(radians(ang))
coseno = cos(radians(ang))
tang = tan(radians(ang))

print('o angulo {:.2f} equivale ao Seno de {:.2f}\nCoseno de {:.2f}\n tangente de {:.2f}.'.format(ang,seno,coseno,tang))
