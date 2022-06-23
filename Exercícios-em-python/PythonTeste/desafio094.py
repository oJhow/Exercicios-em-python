pessoa = dict ()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo[M/F]:')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou F')
    pessoa['idade'] = int(input('idade: '))
    soma+= pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Você quer continuar [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite apenas S ou N.')
    if resp in 'N':
        break
media = soma/len(galera)
print(galera)
print(f'A) foram cadastradas {len(galera)} pessoas.')
print(f'B) a média da idade das pessoas é {media:5.2f}')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end='')
print()
print('D) As pessoas com a idade acima da média são ', end='')
for i in galera:
    if i['idade'] >= media:
        print('   ')
        for k, v in i.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<<<<<encerrado>>>>>')



