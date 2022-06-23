from ex109 import moeda
p = float(input('Digite um valor: R$ '))
print(f'a metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'o valor aumentado em 15% é {moeda.aumentar(p,15, True)}')
print(f'o valor reduzido em 10% é {moeda.diminuir(p,10, True)}')