from ex108 import moeda
p = float(input('Digite um valor: R$ '))
print(f'a metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'o dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'o valor aumentado em 15% é {moeda.moeda(moeda.aumentar(p,15))}')
print(f'o valor reduzido em 10% é {moeda.moeda(moeda.diminuir(p,10))}')