palavras = ('APRENDER','FALAR','ESCUTAR','ESTUDAR','CURSO','LER','OUVIR')

for pos in palavras:
    print(f'\nna palavra {pos} temos: ',end = '')
    for letra in pos:
        if letra.lower() in 'aeiou':

            print(letra,end=' ')
