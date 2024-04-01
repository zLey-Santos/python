frase = str(input("DIGITE UMA FRAAE: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
  inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}')  
if inverso == junto:
  print(f'Temos um palíndromo!')
else:
  print(f'Não temos um palíndromo!')
 