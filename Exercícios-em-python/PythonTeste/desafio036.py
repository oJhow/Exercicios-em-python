import time
casa = float(input('Qual é o valor da casa ? '))
sal = float(input('Qual é o seu salário ? '))
ano = int (input('em quantos anos deseja pagar essa casa ? '))

prest = ano * 12
par = casa/prest
poc = (sal*30)/100

print('Emprestimo bancário')
print('caso o valor da parcela da casa for maior que 30% do salário, o emprestimo será negado')
print('PROCESSANDO VALORES...')
time.sleep(2)
print ('valor da casa {:.2f}R$'.format(casa))
time.sleep(2)
print('salário {:.2f}R$'. format(sal))
time.sleep(2)
print('quantidade de parcelas {}'.format(prest))
time.sleep(2)
if par > poc:
    print('emprestimo negado, o valor da parcela {:.2f}R$, excedeu o valor de 30% do seu salário que é {:.2f}R$'.format(par,poc))
elif par <= poc:
    print ('Emprestimo aprovado, você terá {} prestações e ira pagar {:.2f}R$'.format(prest,par))
    print('parabens pelo investimento!!!')
print('obrigado por nos contactar')

