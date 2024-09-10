palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Curso', 'Grátis', 
            'Estudar', 'Praticar', 'Trabalhar', 'Mercado', 'Programador', 'furacão')

vogais = ('a', 'á', 'à', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í', 'î', 'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û')

for p in palavras:
  print(f'\nNa palavra {p.upper()} temos: ', end='')
  for letra in p:
    if letra.lower() in vogais:
      print(letra.upper(), end=' ')