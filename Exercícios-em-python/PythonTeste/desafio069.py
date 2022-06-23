maior =homem = mulher =  0

while True:
    print('-' * 30)
    idade = int(input('Digite a idade: '))
    sexo = ' '
    c = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        print('-' * 30)

    while c not in 'SN':
        c = str(input('Deseja continuar [S/N] ? ')).strip().upper()[0]

    if idade >= 18:
        maior +=1
    if sexo == 'M':
        homem+=1
    if sexo == 'F':
        if idade <20:
            mulher+=1

    if c == 'N':
        break

print(f'''no total são {maior} com mais de 18 anos.
{homem} homens.
{mulher} mulheres com menos de 20 anos.''')