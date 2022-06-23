s = 0
c = 0
for t in range (1, 501, 2):
    if t % 3 == 0:
        s += t
        c += 1
print('a soma de todos os {} numeros multiplos entre 1 e 500 é {}'.format(c,s))
