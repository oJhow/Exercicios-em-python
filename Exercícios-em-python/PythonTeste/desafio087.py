matriz = [[0,0,0],[0,0,0],[0,0,0]]
somap = somat= mai = 0
for l in range (0,3):
    for c in range (0,3):
        matriz [l] [c]= int (input(f'Digite um valor para a posição [{l},{c}]: '))
        if matriz [l][c] % 2 == 0:
            somap += matriz [l][c]
        if c in [2]:
            somat += matriz[l][c]
print('-='*30)
for l in range(0,3):
    for c in range (0,3):
        print(f'[{matriz [l] [c]:^5}]',end='')
    print()

print(f'A soma dos pares é {somap}.')
print(f'A soma dos valores da terceira coluna é {somat}.')
for c in range (0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz [1][c]

print(f'O maior numero da segunda linha é: {mai}.')
