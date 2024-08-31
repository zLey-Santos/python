lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')

for comida in lanche:
  print(comida)

print(f"_______________")

for cont in range(0, len(lanche)):
  print(f'Eu vou comer {lanche[cont]} na posicao {cont}')

print(f"_______________")

for pos, c in enumerate(lanche) :
 print(f'Eu vou comer: {c} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))