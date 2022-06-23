lista = ('Carne', 20.00,
         'frango',15.00,
         'linguiça',10.00,
         'refrigerante',5.00,
         'cerveja',6.00)
print('-'*40)
print(f'{"Lista de preços":^40}')
print('-'*40)
for pos in range (0, len(lista)):
    if pos % 2 ==0:
        print(f'{lista[pos]:.<30}',end = '')
    else:
        print(f'R$ {lista[pos]:>5.2f}')
print('-'*40)



