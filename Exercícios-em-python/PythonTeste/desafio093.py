jogador = {}
partida = []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
for t in range(tot):
    partida.append(int(input(f'quantos gols {jogador["nome"]} fez na partida {t+1} ?')))
jogador['gols'] = partida[:]
jogador['total'] = sum(partida)
print('-='*28)
print(jogador)
print('-='*28)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*28)
print(f'o {jogador["nome"]} jogou {tot} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'   => na partida {i+1} ele marcou {v} gols')
print(f'foi um total de {jogador["total"]} gols.')
