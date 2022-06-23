from time import sleep
from datetime import date
atual = date.today().year
print('analisador de Idade para se alistar.')


id = int(input('em que ano você nasceu ? '))
sex = str(input('qual é o seu sexo ? ')).lower().strip()
print('Analisando...')
ano = 2021 -id
temp = (ano - 18) * (- 1) * (-1)
sleep(2)
print('você nasceu em {} você tem {} anos em {}.'.format(id,ano,atual))
print('sexo:{}'.format(sex))

if sex == 'masculino':
 if ano == 18 :

    print('Você está na idade ideal para se alistar.')

 elif ano < 18:
    print('Ainda é muito cedo para você se alistar.')
    temp = (ano - 18) * (- 1)

    print('ainda falta {} ano(s) para você se alistar.'.format(temp))
 else:
    print('Você está atrasado em {} ano(s) para se alistar, vá o quanto antes!!!'.format(temp))
    temp = (ano - 18) * (- 1) * (-1)
else:
 print('O alistamento é obrigatório apenas para homens.')

print('caso seja homem, aliste-se no exercito brasileiro, você não tem escolha!!!')

