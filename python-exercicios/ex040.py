# Solicita ao usuário que insira o nome do aluno e o converte para string.
nome = str(input('Nome do aluno: '))

# Define um dicionário com códigos ANSI para cores usadas na formatação de saída.
cores = {
   'NOME': '\033[1:36m',  # Cor azul ciano para destacar o nome do aluno
   'MD': '\033[1:33m',  # Cor amarela para destacar a média
   'RP': '\033[1:31m',  # Cor vermelha para indicar aluno reprovado
   'AP': '\033[1:32m',  # Cor verde para indicar aluno aprovado
   'RC': '\033[1:34m',  # Cor azul para indicar aluno em recuperação
   'FIM': '\033[m'  # Reset a formatação de cores
}

# Solicita ao usuário que digite as notas do aluno e formata a saída com o nome do aluno colorido.
n1 = float(input(f'Digite a primeira nota do aluno {cores["NOME"]}{nome}{cores["FIM"]}: '))
n2 = float(input(f'Digite a segunda nota do aluno {cores["NOME"]}{nome}{cores["FIM"]}: '))

# Calcula a média das notas.
media = (n1 + n2) / 2

# Verifica a situação do aluno com base na média e imprime a mensagem correspondente.
if media >= 7:
   # Se a média for maior ou igual a 7, o aluno é aprovado.
   print(f'O aluno, {cores["AP"]}{nome}{cores["FIM"]},'
         f' teve uma média de {cores["MD"]}{media}{cores["FIM"]} '
         f'e está {cores["AP"]}[-APROVADO-]{cores["FIM"]} ')

elif 7 > media >= 5:
   # Se a média for menor que 7 e maior ou igual a 5, o aluno está em recuperação.
   print(f'O aluno, {cores["RC"]}{nome}{cores["FIM"]},'
         f' teve uma média de {cores["MD"]}{media}{cores["FIM"]} '
         f'e está de {cores["RC"]}[-RECUPERAÇÃO-]{cores["FIM"]} ')

elif media < 5:
   # Se a média for menor que 5, o aluno é reprovado.
   print(f'O aluno, {cores["RP"]}{nome}{cores["FIM"]},'
         f' teve uma média de {cores["MD"]}{media}{cores["FIM"]} '
         f'e está {cores["RP"]}[-REPROVADO-]{cores["FIM"]} ')

else:
   # Se nenhum dos casos acima for válido, imprime uma mensagem de erro.
   print('[ERRO]')
