from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

op = 0
while not op == 5:
    op = int(input('escolha uma opção:\n'
          '[1] somar\n'
          '[2]multiplicar\n'
          '[3] maior\n'
          '[4]novos numeros\n'
          '[5] sair do programa\n'
                   '>>>>> Qual é a sua opção ? '))

    if op == 1:
        soma = n1+n2
        print ('a soma entre o numero {} + {} é igual a {}'.format(n1,n2,soma))


    elif op == 2:
        mult = n1*n2
        print ('a produto dos fatores {} * {} é igual a {}'.format(n1,n2,mult))

    elif op == 3:
        if n1 > n2:
            maior = n1
            print ('o maior numero entre {} e {} é {}'.format(n1,n2,maior))

        else:
            maior = n2
            print('o maior numero entre {} e {} é {}'.format(n1, n2, maior))

    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif op == 5:
        print('finalizando...')
    else:
        print ('opção invalida, tente novamente.')

    sleep(2)



print ('programa finalizado.')


