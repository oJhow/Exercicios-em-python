maior = 0
menor = 0
for pess in range (1,6):
    peso = float (input("Quantos Kgs a {}ª pessoa pesa: ".format(pess)))

    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso



print("O maior peso foi {}Kgs".format(maior))
print("O menor peso foi {}Kgs".format(menor))
