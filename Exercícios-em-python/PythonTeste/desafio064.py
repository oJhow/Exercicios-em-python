cont = n = soma = 0

while n != 999:
    n = int(input('Digite um numero[999 para parar]:'))
    if n != 999:
        soma = n+n
        cont += 1
print('foram digitados {} numeros e a soma entre eles é {}'.format(cont, soma))
