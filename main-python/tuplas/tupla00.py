
# Variável compostas 

lanche = ('Hamburger', 'Suco', 'Pizza', 'Pudim') # Tuplas são IMUTÁVEIS

# Fatiamento
print(lanche[0:2]) 
print(lanche[1:])
print(lanche[-2])
print('Quantidade de lanche', len(lanche))

for c in lanche:
  print('Comida:', c)
