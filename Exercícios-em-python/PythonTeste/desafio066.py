cont = soma = 0

while True :
    n = int (input('Digite um numero ou 999 para parar: '))

    if n == 999:
        break

    soma += n
    cont += 1

print (f'A quantidade de numeros digitados foi {cont} e a soma desses numeros é {soma}.')