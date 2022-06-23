from ex107 import moeda
p = float(input('Digite um valor: R$ '))
print(f'a metade de {p} é {moeda.metade(p)}')
print(f'o dobro de {p} é {moeda.dobro(p)}')
print(f'o valor aumentado em 15% é {moeda.aumentar(p,15)}')
print(f'o valor reduzido em 10% é {moeda.diminuir(p,10)}')