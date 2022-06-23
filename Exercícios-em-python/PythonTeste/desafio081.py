lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continua = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if continua in 'N':
        break
lista.sort(reverse=True)
print(f'foram digitados {len(lista)} valores.')
print(f'A lista de forma decrescente é {lista}.')
if 5 in lista:
    print('o valor 5 está na lista')
else:
    print('o valor 5 não está na lista')