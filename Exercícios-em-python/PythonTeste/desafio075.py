num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))


print (f'Os valores digitados foram: {num}')

print(f'\n o numero nove aparece {num.count(9)} vezes.')
if 3 in num:
    print(f'o numero 3 aparece na {num.index(3)+1}ª posição')
else:
    print('o valor 3 não foi digitado.')
print('Os valores pares digitados foram: ',end ='')
for n in num:
    if n % 2 == 0:
        print(n,end =' ')