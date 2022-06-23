from numpy import mean

p1 = float(input('digite a primeira nota: '))
p2 = float(input('digite a segunda nota: '))

media = mean([p1,p2])

print('a sua média foi de {}'.format(media))

if media < 5:
    print('Você foi reprovado!!')
elif media > 5 and media < 6.9:
    print('Você está de recuperação!')
else:
    print ('você foi aprovado!!')
