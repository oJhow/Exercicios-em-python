lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    s = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
    if s in 'N':
        break
print(f'a lista completa é {lista}')
for n in lista:
    if n % 2 == 0:
        pares.append(n)

    else:
        impares.append(n)

print(f'a lista de pares é {pares}')
print(f'a lista de impares é {impares}')