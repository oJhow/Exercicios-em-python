times = ('Atletico - MG','Flamengo','Palmeiras','Fortaleza','Corinthians'
         ,'Bragantino','Fluminense','America - MG','Atletico - GO','Santos'
         ,'Ceára SC','Internacional','São paulo','Athletico - PR','Cuiabá'
         ,'Juventude','Grêmio','Bahia','Sport recife','chapecoense')

print ('='*300)
print(times)
print ('='*300)
print(f'Os 5 primeiros times são: {times[0:5]}')
print ('='*300)
print (f'os ultimos 4 colocados são: {times[-4:]}')
print ('='*300)
print (f'os times em ordem alfabética são:{sorted(times)}')
print ('='*300)
print(f'a chapecoense está na posição: {(times.index("chapecoense")+1)}')
