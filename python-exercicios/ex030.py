num = int(input('Digite um número: '))

par_impar = num % 2

if par_impar == 0:
    print('\033[1:32m Par \033[m')
else:
    print('\033[1:31m Ímpar\033[m')
