from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)
}
ranking = []
print('valores sorteados')
for k, v in dados.items():
    print(f'{k} tirou {v}.')
    sleep(1)
ranking = sorted(dados.items(),key =itemgetter(1),reverse=True) #itemgetter serve para usar como chave para organizar alguma coisa com base nessa chave
print('== Ranking ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
