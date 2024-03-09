from math import sin, cos, tan, radians
angulo = float(input(f'Digite o valor do ângulo em graus: '))

# Converte o ângulo para radiano, pois as funções trigonométricas em python trabalham com radianos
angulo_rad = radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo
seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print(f'Seno({angulo}\u00b0) = {seno:.2f} \n'
      f'Cosseno({angulo}\u00b0) = {cosseno:.2f} \n'
      f'Tangente({angulo}\u00b0) = {tangente:.2f}')


