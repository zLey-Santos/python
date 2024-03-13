km = float(input('Qual a distancia da sua viagem em Km: '))

km_limit = 200
valor_kmp = 0.50
dis_p = km * valor_kmp

valor_kml = 0.45
dis_l = km * valor_kml

if km <= km_limit:
    print(f'O valor para uma viagem de {km:.0f}Km R${dis_p:.2f}')
elif km > km_limit:
    print(f'O valor para uma viagem de {km:.0f}Km R${dis_l}')

