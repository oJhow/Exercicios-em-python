dia = int(input('Por quantos dias este carro foi alugado ? '))
km = float(input('quantos KMs foram rodados ? '))

aluguel = (dia * 60) + (km * 0.15)

print ('o carro foi usado por {} dias e rodou {:.2f} kms então o valor do aluguel é de {:.2f} R$'.format(dia,km,aluguel))
