time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou ? '))
    partida.clear()
    for t in range(tot):
        partida.append(int(input(f'quantos gols {jogador["nome"]} fez na partida {t+1} ?')))
    jogador['gols'] = partida[:]
    jogador['total'] = sum(partida)
    time.append(jogador.copy())
    while True:
        cont = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! digite apenas sim ou não')
    if cont == 'N':
        break
print('-='*30)
print('cod ', end='')
for k in jogador.keys():
    print(f'{k:<15}',end='')
print()
print('-='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ',end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()
print('-='*40)
while True:
    busca = int(input('Mostrar dados de qual jogador [999 para parar]:'))
    if busca == 999:
        break

    if busca >= len(time):
        print(f'Erro! não existe jogador com o código {busca}')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'no jogo {i+1} marcou {g} gols ')
print('Programa encerrado')
