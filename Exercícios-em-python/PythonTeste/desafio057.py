sexo = str(input("digite seu sexo [M/F]:")).upper().strip()[0]

while sexo not in 'MF':
    sexo = str(input('letra incorreta, digite novamente [M/F]:')).upper()

print('sexo {} registrado '.format(sexo))




