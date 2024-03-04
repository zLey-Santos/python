medida = float(input('Distância em metros: '))
km = medida / 1000     # quilômetros
hm = medida / 100      # hectômetros
dam = medida / 10      # decâmetros
cm = medida * 100      # centímetros
mm = medida * 1000     # milímetros

print(f'A medida de {medida}M,\n'
      f'-corresponde a quilômetros {km}km, \n'
      f'-corresponde a hectômetros {hm}hm, \n'
      f'-corresponde a decâmetros {dam:.3f}dam, \n'
      f'-corresponde a centímetros {cm:.0f}cm, \n'
      f'-corresponde a milímetros {mm:.0f}mm')
