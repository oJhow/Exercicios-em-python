print('{:=^40}'.format(' LOJAS oJhow '))
val = float (input('Valor da compra R$ '))
form = int (input('''Forma de pagamento.
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4]3x ou mais no cartão
escolha uma das opções pelo numero: '''))

print('o valor da compra foi {:.2f}'.format(val))
print('a forma de pagamento escolhida foi {}'.format(form))

if form == 1:
    print('à vista no dinheiro/cheque 10% de desconto')
    desc = val-(val * 0.10)
    print('o valor da compra com 10% de desconto é R${:.2f}'.format(desc))
elif form == 2:
    print('à vista no cartão 5% de desconto')
    desc = val - (val * 0.05)
    print('o valor da compra com desconto é R${:.2f}'.format(desc))
elif form == 3:
    print('2x no cartão.')
    parc = val/2
    print('o valor da compra é de R${:.2f} em duas parcelas de R${:.2f}'.format(val, parc))
else:
    if form ==4:
        p = int(input('Quantas parcelas ? '))
        p2 = val+(val*0.20)
        p3 = p2/p

        print ('sua compra será parcelada em {}x de R${:.2f} com juros'.format(p, p3))
    else:
        print('opção invalida, tente novamente')

print('obrigado pela preferencia.')




