p = str(input('digite uma frase: ')).strip().upper()
palavras = p.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(' o inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo')
else:
    print('não temos um palindromo')


