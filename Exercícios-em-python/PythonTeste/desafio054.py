from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range (1,8):
    ano = int(input("Em que ano a {}ª pessoa nasceu: ".format(c)))
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1


print("{} pessoas são maiores de idade.".format(totmaior))
print("{} pessoas são menores de idade.".format(totmenor))