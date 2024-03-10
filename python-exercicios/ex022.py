# Solicita ao usuário que insira seu nome completo e remove espaços em branco extras com strip()
nome = str(input('Digite seu nome completo: ')).strip()

# Imprime informações sobre o nome inserido pelo usuário
print(f'Analisando seu nome...\n'
      f'Seu nome em maiúsculas é {nome.upper()}\n'  # Transforma o nome em maiúsculas
      f'Seu nome em minúsculas é {nome.lower()}\n'  # Transforma o nome em minúsculas
      f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras\n'  # Conta as letras desconsiderando espaços em branco
      f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras')  # Extrai o primeiro nome e conta suas letras

'''
import re
nome0 = re.sub(r'/s+', '', nome) inverter a barra
Remover todos os espaços de uma string com o módulo re
'''

# O código comentado mostra como remover todos os espaços de uma string usando o módulo re.
# No entanto, não está sendo usado neste script.
