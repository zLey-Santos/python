# Imprime uma linha de separação para destacar o título do programa.
print('-=-' * 10)
# Imprime o título do programa.
print('Analisador de Triângulos')
# Imprime outra linha de separação para destacar o título do programa.
print('-=-' * 10)

# Solicita ao usuário que insira os comprimentos dos lados do triângulo e os converte em float.
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo  segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

print('-=-' * 10)
# Verifica se as condições para formar um triângulo são atendidas.
tri1 = r1 < r2 + r3
tri2 = r2 < r1 + r3
tri3 = r3 < r1 + r2

# Verifica se todas as condições para formar um triângulo são verdadeiras.
if tri1 and tri2 and tri3:
    # Se todas as condições forem verdadeiras, imprime que os segmentos podem formar um triângulo.
    print('\033[1:34m Os seguimentos PODEM FORMAR um triângulo! \033[m ')
else:
    # Se pelo menos uma das condições não for verdadeira, imprime que os segmentos não podem formar um triângulo.
    print('\033[1:31mOs seguimentos NÂO FORMAM um triângulo!\033[m')

# Imprime uma mensagem de fim com uma seta dupla no início e no final.
print('<-' * 5 + ' FIM ' + '->' * 5)
