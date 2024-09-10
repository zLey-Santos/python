listagem = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90,
            'Estojo', 16.70, 'Trnaferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 122.35, 'Canetas', 22.35, 'Livro', 34.90)
print('-' *38)
print(f'{'_'*13}Lista Escolar{'_'*12}')
print('-' *38)

for pos in range(0, len(listagem)):
  if pos % 2 == 0:
    print(f'{listagem[pos]:_<30}', end='')
  else:
    print(f'{listagem[pos]:>7.2f}€')
print('-' *38)
