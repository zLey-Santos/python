print('-=-' * 10)
print('Analisador de Triângulos')
print('-=-' * 10)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo  segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

tri1 = r1 < r2 + r3
tri2 = r2 < r1 + r3
tri3 = r3 < r1 + r2

if tri1 and tri2 and tri3:
   print('Os seguimentos PODEM FORMAR um triângulo! ')
else:
   print('Os seguimentos NÂO FORMAM um triângulo!')

print('<-' * 5 + ' FIM ' + '->' * 5)
