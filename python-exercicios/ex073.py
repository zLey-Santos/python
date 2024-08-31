times =('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 
        'Atlético', 'Botafogo', 'Atlético-PR', 'Bhaia', 'São Paulo', 'Fluminense', 'Sport Recife', 
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')


for t in times:
  print(f'{t}')
print('-=' * 35)
print(f'Lista de times: {times}')
print('-=' * 35)
print('')
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=' * 35)
print('')
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 35)
print('')
print(f'Times em ordem alfabético: {sorted(times)}')
print('-=' * 35)

print(f'O Chapecoense está na {times.index("Chapecoense")} posição ')