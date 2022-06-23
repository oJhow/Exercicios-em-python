def metade(n=0,formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, x=0, formato=False):
    res = n + (n * x / 100)
    return res if not formato else moeda(res)


def diminuir(n=0, x=0, formato=False):
    res = n - (n * x / 100)
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def resumo(n=0, xa = 10, xd = 5, formato=False):
    print('-'*30)
    print('Resumo de valores'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t\t\t{moeda(n)}')
    print(f'metade do preço: \t\t\t{metade(n,True)}')
    print(f'dobro do preço: \t\t\t{dobro(n,True)}')
    print(f'taxa de {xa}% aumento de: \t{aumentar(n, xa,True)}')
    print(f'taxa de {xd}% redução de: \t{diminuir(n,xd,True)}')
    print('-'*30)
