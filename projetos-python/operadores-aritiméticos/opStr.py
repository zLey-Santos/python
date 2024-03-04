# Podemos usar Operadores Aritméticos para outros fins.
# Podemos usar de várias formas com vários operadores diferentes .format() pode causar um aviso de erro.
# > Ajusta ao final de x caracteres,
# < Ajusta para o início deixando x caracteres ao fim,
# ^ Justa ao centro,
# OBS: Caso queira adicionar um caractere antes e depois do TEXTO, basta {nomeVariable: character^valor}
# A sintaxe é {variável: símboloOPA valorNum} - {nome:*^10}
# Caso a quantidade de caracteres for a mesma que o espaço, ele não adiciona os Símbolos.
# Exemplo: {nome:*^6} Wesley == 6 caracteres, a saída seria Wesley.
# Exemplo: {nome:*^6} zLey == 6 caracteres, *zLey* ou ley, a saída seria *ley**

nome = input('Qual o seu nome? ')
print(f'Prazer em te conhecer: {nome:*^6}!')
