print('-'*30)
print('LOJA DO oJHOW')
print('-'*30)
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: ')).strip()
    valor = float(input('Valor do produto: '))
    cont +=1
    total += valor

    c = '  '
    while c not in'SN':
        c = str(input('Quer continuar [S/N]? ')).strip().upper()[0]

    if valor >= 1000:
        totmil += 1
    if cont ==1 or valor < menor:
        menor = valor
        barato = produto


    if c =='N':
        break
print(f'''O total da compra foi: {total:.2f}
nessa compra existem {totmil:.2f} produtos com valor maior ou igual a R$ 1000,00
o produto com o menor valor foi um(a){barato} e o valor foi  R${menor:.2f}.''')




