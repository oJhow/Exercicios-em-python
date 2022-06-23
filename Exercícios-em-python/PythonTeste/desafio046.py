from time import sleep

import emoji


print('CONTAGEM REGRESSIVA PARA FOGOS ESTOURANDO')
for f in range (10,-1,-1):
    print(f)
    sleep(1)
print('Fogos estourando!!')
print(emoji.emojize(':fireworks:'*10))