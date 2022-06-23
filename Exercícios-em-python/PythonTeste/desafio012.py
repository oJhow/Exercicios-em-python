p = float(input('digite o valor do produto desejado:'))

d = p*0.05

vf = p - d


print('o valor do produto é de R${}, com 5% de desconto é R${:.2f}.'.format(p, vf))
