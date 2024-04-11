# Exibe uma mensagem de título para o gerador de Progressão Aritmética (PA)
print('Gerador de PA')
print('=' * 20)

# Solicita ao usuário o primeiro termo e a razão da PA
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

# Inicializa o primeiro termo da PA
termo = primeiro

# Inicializa o contador para controlar os termos da PA
cont = 1

# Loop while para gerar e exibir os 10 primeiros termos da PA
while cont <= 10:
    # Exibe o termo atual da PA
    print(f'{termo}', end=' -> ')
    
    # Calcula o próximo termo da PA somando a razão ao termo atual
    termo += razao
    
    # Incrementa o contador para controlar o número de termos exibidos
    cont += 1

# Exibe uma mensagem indicando o término da PA
print('PA finalizada!')
