v = float(input("quantos KM's terá sua viagem ?"))

print("a viagem terá {:.2f} KM's.".format(v))
if v < 200.00:
    print('será cobrado 0.50 R$ por KM rodado')
    print('o Valor da sua viagem será {:.2f} R$.'.format((v*0.50)))
else:

    print('será cobrado 0.45 R$ por KM rodado')
    print('o valor da sua viagem será {:.2f} R$'.format((v*0.45)))