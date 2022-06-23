aluno = {}
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input(f'média de {aluno["nome"]}: '))
print('-='*30)
if aluno['media'] < 7 and aluno['media'] > 5 :
    aluno['situação'] = 'recuperação'
elif aluno['media'] < 5:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'aprovado'
for f, v in aluno.items():
    print(f'- {f} é igual a {v}')
    