c = float(input('Informe a Temperatura em \u2103 '))
tc = ((c * 9) / 5) + 32
print(f'A temperatura de {c}\u2103 corresponde a temperatura de {tc:.2f}\u2109')

f = float(input(f'Informe a Temperatura em \u2109 '))
tf = (f - 32) * 5/9
print(f'A temperatura de {f}\u2109 corresponde a temperatura de  {tf:.2f}\u2103 ')
