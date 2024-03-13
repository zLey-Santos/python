km = int(input('Qual a velocidade do carro: '))

limit = 80
fine_price = 7
fine = (km - limit) * 7

if km > limit:
    print(f'Excedeu o limite da via de \033[0;33;3m{limit}Km/h, \033[0;0;0m  sua velocidade foi de \033[0;33;3m{km}Km/h \033[0;0;0m \n'
          f'Pagara uma multa de \033[0;33;3mR${fine_price}\033[0;0;0m por quilometro excedido \n'
          f'sua multa sera aplicada no valor de \033[0;33;3mR${fine:.2f}\033[0;0;0m')
else:
    print(f'Sua velocidade é {km}Km/h (não há excedente)')
