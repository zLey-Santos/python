# Importa o módulo 'date' da biblioteca 'datetime', que permite trabalhar com datas.
from datetime import date

# Obtém o ano atual.
ano_atual = date.today().year
print(f'{"==" * 10} ALISTAMENTO MILITAR {"==" * 10}')

# Solicita ao usuário que digite o ano de nascimento e converte para inteiro.
ano_nascimento = int(input('Digite sua data de nascimento: '))
# Calcula a idade subtraindo o ano de nascimento do ano atual.
idade = ano_atual - ano_nascimento
# Imprime a mensagem indicando a idade atual.
print(F'Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}.')

# Verifica se a idade é igual a 18 anos.
if idade == 18:
   # Se a idade for igual a 18, imprime a mensagem para se alistar imediatamente.
   print('Você tem que se alistar IMEDIATAMENTE! ')
# Verifica se a idade é menor que 18 anos.
elif idade < 18:
   # Se a idade for menor que 18, calcula o tempo que falta para o alistamento e imprime a mensagem correspondente.
   saldo = 18 - idade
   ano = ano_atual + saldo
   print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para se alistar. \n'
         f'Seu alistamento será em {ano}.')
# Se a idade for maior que 18 anos.
elif idade > 18:
   # Se a idade for maior que 18, calcula há quantos anos deveria ter ocorrido o alistamento e imprime a mensagem correspondente.
   saldo = idade - 18
   ano = ano_atual - saldo
   print(f'Você já deveria ter se alistado há {saldo} anos atrás. \n'
         f'O seu alistamento foi em {ano}.')
else:
   # Se nenhuma das condições acima for válida, imprime uma mensagem de erro.
   print('[ERRO!!!]')
