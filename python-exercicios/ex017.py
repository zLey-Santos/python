from math import sqrt, hypot
cateto_oposto = float(input('Digite o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Digite o comprimento do cateto adjacente: '))

#hipotenusa = sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'O comprimento entre cateto oposto {cateto_oposto} eo cateto adjacente {cateto_adjacente} tem o valor da hipotenusa de {hipotenusa:.2f}')
