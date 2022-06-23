def notas(*n, sit=False):
    """
    Função para analisar notas e situações de alunos
    :param n: Notas
    :param sit: Função para saber a situação ounão
    :return: dicionariocom as informações da nota.
    """
    turma = {}
    maior = 0
    menor = 0
    cont = 0
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n) / len(n)
    if sit:
        if turma['media'] < 5:
            turma['Situação'] = 'Ruim!'
        elif 5 <= turma['media'] < 7:
            turma['Situação'] = 'Razoavél'
        else:
            turma['Situação'] = 'Boa!'
    return turma


# Programa principal
resp = notas(6, 1, 3, 4, 5, 5, sit=True)
print(resp)
help(notas)