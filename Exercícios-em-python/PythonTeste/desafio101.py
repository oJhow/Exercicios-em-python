def voto(id=0):
    from datetime import datetime
    print('-' * 40)
    id = datetime.now().year - nasc
    if id < 16:
        return f'com {id} anos o Voto é negado.'
    elif 16 <= id < 18 or id > 65:
        return f'com {id} anos o voto é opicional.'
    elif 18 <= id < 65:
        return f'com {id} anos o Voto é obrigatório.'


# programa principal
nasc = int(input('Digite o seu ano de nascimento: '))
print(voto(nasc))
