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


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
