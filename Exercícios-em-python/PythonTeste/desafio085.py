principal = [[],[]]
v = 0
for n in range (0,7):
    v = int(input(f'Digite o {n+1}º valor:'))
    if v % 2 == 0:
        principal[0].append(v)
    else:
        principal[1].append(v)
print(f'Os numeros pares são {principal[0]} e os impares são {principal[1]}.')
