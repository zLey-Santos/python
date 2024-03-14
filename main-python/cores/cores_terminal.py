print('\033[31mOlá, mundo!\033[m')
print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[7;31;43mOlá, mundo!\033[m')
print('\033[7;mOlá, mundo!\033[m')

cores = {
    'limpa': '\033[m',
    'texto': '\033[31m'
}

nome = 'Wesley'
print(f'Olá {cores['texto']}{nome}{cores['limpa']}, prazer em te conhecer!!! ')
