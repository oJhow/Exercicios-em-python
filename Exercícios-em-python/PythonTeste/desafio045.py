import random
from time import sleep
print('jogo jokenpô')
itens = ('pedra', 'papel', 'tesoura')
jog = int (input('''suas opções:
[0] pedra
[1] papel
[2] tesoura
escolha uma delas: '''))

pc = random.randint(0,2)
print('o computador jogou {}.'.format(itens[pc]))
print('O jogador jogou {}.'.format(itens[jog]))

print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô')
sleep(1)

if jog == pc:
    print('empate')
elif jog == 0 and pc == 1:
    print('o computador ganhou, papel ganha de pedra.')
elif jog ==1 and pc == 0:
    print('você ganhou, papel ganha de pedra.')
elif jog == 0 and pc == 2:
    print('você ganhou, pedra ganha de tesoura.')
elif jog == 2 and pc ==0:
    print ('o computador ganhou, pedra ganha de tesoura.')
elif jog == 1 and pc == 2:
    print('o computador ganhou, tesoura ganha de papel.')
elif jog ==2 and pc ==1:
    print ('você ganhou, tesoura ganha de papel.')
else:
    print('opção invalida, digite entre 0 e 1.')
print('Obrigado por jogar.')







