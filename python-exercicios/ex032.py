# Ano Bissexto
from datetime import datetime

print('-=-' * 22)
print('\033[4mAnalisando se o ano é \033[1:35mBISSEXTO...\033[m')
print('')

# Variáveis de cores
cores = {
    'titulo': '\033[1:30:46m',
    'limpa': '\033[m',
    'texto_b': '\033[1:35m',
    'ano_b': '\033[1:33m',
    'ano_nb': '\033[1:31m'
}

ano = int(input(f'{cores["titulo"]}Que ano deseja analisar? (Coloque 0 para analisar o ano atual):\033[m '))

ano_atual = datetime.now().year
ano_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

print('')

if ano == 0:
    print(f'O ano atual a ser analisado é:'
          f' {cores["ano_b"]}{ano_atual}{cores["limpa"]}')
    if ano_bissexto:
        print(f'O ano de{cores["ano_b"]} {ano_atual}{cores["limpa"]}'
              f' é um ano'
              f'{cores["texto_b"]} '
              f'bissexto'
              f'{cores["limpa"]}.')
    else:
        print(f'O {cores["ano_nb"]}{ano_atual}{cores["limpa"]}'
              f' não é um ano bissexto.')
else:
    if ano_bissexto:
        print(f'O ano de{cores["ano_b"]}{ano}{cores["limpa"]}'
              f' é um ano bissexto.')
    else:
        print(f'O ano de '
              f'{cores["ano_nb"]}{ano}{cores["limpa"]}, '
              f'não é um ano bissexto.')

print('-=-' * 22)
print('\033[7:31:40m FIM DA ANÁLISE...\033[m')
