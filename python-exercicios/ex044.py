print(f'{"=="*10}LOJA DO [z]{"=="*10}')

# Solicita ao usuário que insira o preço das compras
preco = float(input('Preço das compras: '))

# Imprime o cabeçalho das formas de pagamento
print(f'{"$-"*5}_FORMAS DE PAGAMENTO_{"-$"*5}')
print('[1] à vista dinheiro/cheque: 10% de desconto \n'
      '[2] à vista no cartão: 5% de desconto \n'
      '[3] em até 2x no cartão: preço formal \n'
      '[4] 3x ou mais no cartão: 20% de juros')

# Solicita ao usuário que escolha a opção de pagamento
opc = int(input('Qual a opção de pagamento: '))

# Verifica a opção de pagamento escolhida e executa a ação correspondente
if opc == 1:
   # Calcula o desconto de 10% para pagamento à vista em dinheiro ou cheque
   avista = (preco * 10 / 100)
   avista_desc = preco - (preco * 10 / 100)
   # Imprime o valor da compra com desconto
   print(f'O valor da sua compra é {preco:.2f}€ menos 10% desconto {avista:.2f}€ o valor final será de: {avista_desc:.2f}€.')
elif opc == 2:
   # Calcula o desconto de 5% para pagamento à vista no cartão
   avista_cartao = (preco * 5 / 100)
   cartao_desc = preco - (preco * 5 / 100)
   # Imprime o valor da compra com desconto
   print(f'Em cartão o valor da sua compra é {preco:.2f}€ menos 5% de desconto {avista_cartao:.2f}€ '
         f'o valor final será de: {cartao_desc:.2f}€.')
elif opc == 3:
   # Calcula o valor das parcelas em até 2x no cartão
   cartao_2x = preco / 2
   # Imprime o valor das parcelas
   print(f'Em cartão o valor será parcelado em 2x de {cartao_2x:.2f}€ o valor final será de {preco:.2f}.')
elif opc == 4:
   # Solicita ao usuário que insira a quantidade de parcelas
   parcelas = int(input('Quantas parcelas: '))
   # Calcula o valor das parcelas em 3x ou mais no cartão com juros de 20%
   juros = (preco * 20 / 100)
   cartao_x3 = (preco + juros) / parcelas
   valor_final = preco + (preco * 20 / 100)
   # Imprime o valor das parcelas com juros
   print(f'Em cartão o valor será parcelado em {parcelas}x de {cartao_x3:.2f}€ com juros de 20% {juros:.2f}€ '
         f'valor final de {valor_final:.2f}€.')
