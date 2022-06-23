def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, x=0):
    res = n + (n * x / 100)
    return res


def diminuir(n=0, x=0):
    res = n - (n * x / 100)
    return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
