from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando valores!')
    print('-='*10)
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='')
        sleep(0.3)
    print('\nPronto!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista} temos a soma {soma}.')

#programa principal
numeros = []
sorteia(numeros)
somapar(numeros)
