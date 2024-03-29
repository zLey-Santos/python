from time import sleep
import emoji

print(f'{'==' * 10}Contagem Regressiva{'==' * 10} ')

for cont in range(10, - 1, -1):
   print(cont)
   sleep(1)
print(emoji.emojize(':sparkler: Feliz Ano Novo!!! :sparkler:'))

