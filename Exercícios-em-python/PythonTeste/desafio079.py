lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print(' valor adicionado com sucesso.')
    else:
        print('Valor duplicado, não será adicionado.')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar :[S/N]')).strip().upper()[0]
    if continuar in 'N':
        break
lista.sort()
print(f'Os numeros digitados foram {lista}')
