def fatorial(num=1, show = False):
    """
    -> calcula o fatorial de um numero
    :param num: o numero a ser calculado
    :param show: (opicional) mostra ou não o calculo
    :return:retorna o fatorial de num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c,end='')
            if c > 1:
                print(f'{c} x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


# programa principal
print(fatorial(5, True))
help(fatorial)
