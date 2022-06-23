lista = []
maior = 0
menor = 0


for c in range (0,5):
    lista.append( int(input(f'Digite um valor para a posição {c}:')))

    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c]< menor:
            menor = lista [c]
print(f'Os valores digitados foram: {lista}')


print(f'O maior valor digitado foi {maior} e ele aparece na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')

print(f'\no menor valor digitado foi {menor} e ele aparece na posição ',end='')
for i, v in enumerate(lista):
    if v==menor:
        print(f'{i}...',end='')