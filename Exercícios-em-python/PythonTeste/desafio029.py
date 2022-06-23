v = float(input('qual velocidade você passou no radar: '))

if v > 80:
    print('você foi multado')
    print('o Valor da sua multa é: {:.2f} R$'.format((v-80)*7))
else:
    print('tenha um bom dia, dirija com segurança!')
