cont = 0
menor = 0
maior = 0
media = 0
soma = 0
r = 's'

while r in 'sS':
    num = int(input('Digite um numero:'))

    r = str(input('Quer continuar [S/N] ? ')).upper().strip()[0]

    cont +=1
    soma+=num



    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
media = soma/cont
print ('numeros digitados {}\nmenor {}\nmaior {}\nmédia {:.2f}'.format(cont,menor,maior,media))




