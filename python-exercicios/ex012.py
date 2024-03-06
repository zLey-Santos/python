val = float(input('Valor do produto: R$'))
desc = (5 / 100) * val
val_final = val - desc

print(f'O produto custava R${val}, na promoção de 5% vai custar apenas R${val_final:.2f} \n'
      f'Foram R${desc:.2f} de desconto direto para você.')
