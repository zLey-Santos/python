# Calculando a temperatura de ºC para ºF ( T(ºF) = T(ºC) \times \frac{9}{5} + 32 )
celsius = float(input('Digite a temperatura em \u2103: '))
T = (celsius * 9/5) + 32
print(f'A temperatura em \u2109 é {T:.1f}')

print('__________________________________________________')

# Calculando a temperatura de ºF para ºC ( T(ºF) = T(ºC) \times \frac{9}{5} + 32 )
fahrenheit = float(input('Digite a temperatura em \u2109: '))
TT = (fahrenheit - 32) * 5/9
print(f'A temperatura em \u2103 é {TT:.1f}')
