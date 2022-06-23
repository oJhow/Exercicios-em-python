def leiaint(msg):
    '''
    Função leiaint serve para ler um numero inteiro, caso não seja
    inteiro ele mostrara uma meensagem de erro.
    :param msg: conteúdo string dentro da variável
    :return: retorna o numero inteiro
    '''
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mErro, digite um numero inteiro valido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de tados interrompida pelo usuário.')
            return

        else:
            return n


def leiafloat(msg):
    '''
    função leiafloat serve para ler um numero real, caso não seja
    real ele mostrara uma mensagem de erro.
    :param msg: string dentro da varável.
    :return: retorna o numero real
    '''
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mErro, Digite um numero real válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return num


#programa principal
n1 = leiaint('Digite um numero inteiro: ')
print(f'Você digitou o numero {n1}')
n2 = leiafloat('Digite um numero real:')
print(f'Você digitou o numero {n2}')
