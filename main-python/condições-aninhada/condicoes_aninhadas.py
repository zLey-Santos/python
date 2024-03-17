city = str(input('Qual a sua cidade? '))

# Condição simples.
if city == 'Lisboa':
   print('Que cidade maneira!')
print('Tenha uma boa estadia em {}!'.format(city))

# Estrutura condicional composta.
city1 = str(input('Qual a sua cidade? '))

if city1 == 'Cascais':
   print('Que cidade boa de viver!')
else:
   print('É uma boa cidade!')

print('Tenha uma boa estadia em {}!'.format(city1))

# Estrutura condicional aninhada.
nome = str(input('Qual é o seu nome? '))

if nome == 'Wesley':
   print('Nome mais lindo!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
   print('O seu nome é bem popular!')
else:
   print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
