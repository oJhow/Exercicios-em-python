maior = 0
menor = 0
soma = 0
media = 0
nomem = ''
mulher = 0
for p in range (1,5):
    print('-----{}ª pessoa-----'.format(p))
    nome = str(input('Digite o seu nome: '))
    idade = int (input('digite sua idade: '))
    sexo = str(input('Sexo(M/F):')).upper()
    soma = soma + idade

    if p == 1 and sexo in 'Mm':
        maior = idade
        nomem = nome
    if sexo in 'Mm' and idade >maior:
        maior = idade
        nomem = nome
    if p == 1 and sexo in 'Ff':
        menor = idade
        mulher = p
        if sexo in 'Ff' and menor < 20:

            mulher += 1




media = soma/4

print('a media de idade do grupo é de {}.'.format(media))
print('O nome do homem mais velho é {}'.format(nomem))
print('a quantidade de mulheres que tem menos de 20 anos é {}'.format(mulher))
