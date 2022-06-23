from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome:'))
dados['idade'] = int(input('Ano de nascimento:'))
dados['idade'] = datetime.now().year - dados['idade']
dados['ctps'] = int(input('Carteira de trabalho(0 caso não tenha):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação:'))
    dados['salario'] = float (input('Sálario:'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print('-='*30)
for k,v in dados.items():
    print(f' - {k} tem o valor {v}.')
