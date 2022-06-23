alt = float(input('Digite a sua altura: '))
peso = float (input('digite o seu peso: '))

imc = peso/(alt**2)

print('O seu IMC é {:.2f}.'.format(imc))

if imc < 18.5:

    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('você está no peso ideal.')
elif imc >=25 and imc < 30:
    print ('você está com sobrepeso.')
elif imc >=30 and imc < 40:
    print('Você está com obesidade.')

else:
    print('você está com obesidade mórbida.')
print('tchau.')
