print(' O valor da diária do veiculo é de R$60,00 \n '
      'O valor por quilometro rodado é de R$0,15')
print('-' * 20)
carro_dia = int(input('Quantos dias o veiculo foi alocado? '))
km = float(input('Quantos Km foram rodados? '))

val_dia = carro_dia * 60
print(f'o valor de {carro_dia} dias de aluguel é de R${val_dia:.2f}')

val_km = km * 0.15
print(f'O valor dos {km:.0f}Km rodados é de R${val_km:.2f} ')

tot = val_dia + val_km
print(f'O valor total entre a diária de R${val_dia:.2f}'
      f' e o valor total de R${val_km:.2f} dos quilômetros rodados é de R${tot:.2f} ')
