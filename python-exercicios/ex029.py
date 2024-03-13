km = int(input('Qual a velocidade do carro: '))

limit = 80
fine_price = 7
fine = (km - limit) * 7

if km > limit:
    print(f'Excedeu o limite da via de {limit}Km/h, sua velocidade foi de {km}Km/h \n'
          f'Pagara uma multa de R${fine_price} por quilometro excedido \n'
          f'sua multa sera aplicada no valor de R${fine}')
else:
    print(f'Sua velocidade é {km}Km/h (não há excedente)')
