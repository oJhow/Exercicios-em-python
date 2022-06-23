temp = []
principal = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('peso: ')))
    if len(principal) == 0:
        mai = men = temp[1]
    else:
        if temp [1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    c = str(input('quer continuar [S/N]:  ')).strip().upper()[0]
    principal.append(temp[:])
    temp.clear()
    if c in 'N':
        break
print(principal)
print(f'foram cadastradas {len(principal)} pessoas.')
print(f'O maior peso cadastrado foi {mai:.2f}. Peso de ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}] ',end='')
print()
print(f'O menor peso cadastrado foi {men:.2f}. Peso de ',end='')
for j in principal:
    if j[1] == men:
        print(f'[{p[0]}] ',end='')
print()

