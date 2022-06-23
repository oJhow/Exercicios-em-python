nome = str(input('Digite seu nome: ')).strip().lower()

div = nome.split()

print('O seu primeiro nome é: {}'.format(div[0]))
print('O seu ultimo nome é: {}'.format(div[len(div)-1]))

