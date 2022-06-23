t = int(input('digite um numero que queira saber a tabuada:'))

for c in range(0,11):
    a = t * c
    print('tabuada {} x {:2} = {}'.format(t,c, a))
print('FIM')
