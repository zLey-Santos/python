from random import randint
from time import sleep # Biblioteca de timeout

print('-=-' * 20)
print('Vou pensar em um número entre (0 e 5). Tente adivinhar... ')
print('-=-' * 20)

num_cpu = randint(0, 5)
num_user = int(input('O número escolhido foi: '))
print('ANALISANDO...')
sleep(2)
if num_user > 5:
    print('Por favor, insira um número válido. ')
elif num_user == num_cpu:
    print(f'Parabéns! Você adivinhou o número corretamente {num_cpu}. ')
else:
    print(f'Tente outra vez. O número correto era {num_cpu} e não {num_user}.')
