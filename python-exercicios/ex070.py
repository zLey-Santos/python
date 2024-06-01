# Inicializa os contadores para:
# totP - soma total dos preços dos produtos
# totMil - número de produtos que custam mais de R$1000
# produtoBarato - nome do produto mais barato
totP = totMil = produtoBarato = 0
menorPreco = float('inf')  # Inicializa o menor preço com um valor infinito
print('-' * 30)
print('LOJA DO JOKER')
print('-' * 30)
# Loop infinito para coletar dados até que o usuário decida parar
while True:
    # Solicita o nome do produto
    produto = str(input('Nome do produto: '))
    
    # Solicita o preço do produto e converte a entrada para um float
    preco = float(input('Preço do produto: R$'))
    
    # Adiciona o preço do produto ao total gasto
    totP += preco
    
    # Verifica se o preço do produto é maior ou igual a R$1000
    if preco >= 1000:
        totMil += 1  # Incrementa o contador de produtos que custam mais de R$1000
    
    # Verifica se este é o produto mais barato até agora
    if preco < menorPreco:
        menorPreco = preco
        produtoBarato = produto
    
    # Inicializa a variável 'resp' com um espaço em branco
    resp = ' '
    # Loop para garantir que o usuário escolha 'S' para sim ou 'N' para não
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    # Verifica se o usuário escolheu parar
    if resp == 'N':
        break  # Interrompe o loop se o usuário escolher parar
print('-' * 20)
# Imprime o total gasto, o número de produtos acima de R$1000, e o produto mais barato
print(f'Total gasto nessa compra: R${totP:.2f}')
print('-' * 30)
print(f'Produtos que custaram mais de R$1000.00: {totMil}')
print('-' * 30)
print(f'O produto mais barato: {produtoBarato}')
print('-' * 30)