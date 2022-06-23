lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('nota 1: '))
    nota2 = float(input('nota 2: '))
    media = (nota1+nota2)/2
    lista.append([nome,[nota1,nota2],media])
    continua = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if continua in 'N':
        break
print('-='*28)
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-'*26)

for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8}')

while True:
    print('-'*64)
    ind = int(input('escolha o numero do aluno para saber a nota [999 para parar]: '))
    if ind == 999:
        print('Encerrando...')
        break
    if ind <= len(lista) - 1:
        print(f'as notas do aluno(a) {lista[ind][0]} é {lista[ind][1]}')
print('Bons estudos.')
