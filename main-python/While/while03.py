n = 1
par = impar = 0

# O loop while continuará executando enquanto a condição n != 0 for verdadeira.
while n != 0:
  n = int(input('Digite um número: '))  # Solicita ao usuário um número inteiro.
  if n != 0:
    if n % 2 == 0:
      par += 1  # Se o número digitado for par, incrementa o contador de pares.
    else:
      impar += 1  # Se o número digitado for ímpar, incrementa o contador de ímpares.

# Quando o usuário digitar 0, a condição n != 0 se tornará falsa, encerrando o loop.
# Em seguida, exibe a contagem de números pares e ímpares digitados.
print(f'Você digitou {par} números pares e {impar} números ímpares.')


'''
O módulo while em Python é uma estrutura de controle de fluxo que permite executar repetidamente um bloco de código enquanto uma condição especificada for verdadeira.
'''