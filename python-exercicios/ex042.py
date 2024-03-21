# Solicita ao usuário que insira os três segmentos do triângulo e converte-os para float.
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verifica se cada segmento é menor que a soma dos outros dois segmentos.
tri1 = r1 < r2 + r3
tri2 = r2 < r1 + r3
tri3 = r3 < r1 + r2

# Verifica se os três segmentos formam um triângulo.
if tri1 and tri2 and tri3:
    # Se os segmentos formam um triângulo, imprime que os segmentos podem formar um triângulo.
    print('Os segmentos PODEM FORMAR um triângulo! ', end='')
    # Verifica o tipo de triângulo com base na medida dos segmentos.
    if r1 == r2 == r3:
        # Se todos os lados forem iguais, o triângulo é equilátero.
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        # Se todos os lados forem diferentes, o triângulo é escaleno.
        print('ESCALENO')
    else:
        # Se pelo menos dois lados forem iguais, o triângulo é isósceles.
        print('ISÓSCELES')
else:
    # Se os segmentos não formarem um triângulo, imprime que não formam um triângulo.
    print('Os segmentos acima NÃO FORMAM um triângulo!')
