from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 20)
    print('\nAnalisando os numeros.')
    sleep(2.5)

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'foram informados {cont} valores.')
    print(f'O maior valor informado foi {maior}')


# programa principal
maior(1, 5, 8, 6, 7, 9, 4)
maior(3, 4, 7, 0, 9)
maior(1, 2)
maior(9)
maior(0)
