nome = str(input('digite seu nome completo:')).strip()

ma = nome.upper()
mi= nome.lower()
sesp = nome.split()
esp = ''.join(sesp)
a=len(esp)
p = len(sesp[0])

print('{}\n{}\n{}\nTotal de caracteres sem espaço:{}'
       '\nquantas letras tem o primeiro nome:{}'.format(nome,ma,mi,a, p))