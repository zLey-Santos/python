import random

print('Tente adivinhar o número entre 1 e 5: ')

num_cpu = random.randint(1, 5)

num_user = int(input('O número escolhido foi: '))
if num_user > 5:
    print('Por favor, insira um número válido. ')
elif num_user == num_cpu:
    print(f'Parabéns! Você adivinhou o número corretamente {num_cpu}. ')
else:
    print(f'Tente outra vez. O número correto era {num_cpu}')
