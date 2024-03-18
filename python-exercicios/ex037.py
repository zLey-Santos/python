print(f'{"<-" * 7} \033[34mCONVERSOR DE BASE NÚMERICA\033[m {"->" * 7}')
# Solicita ao usuário que insira um valor inteiro e o converte para inteiro.
base_numerica = int(input('Digite um valor inteiro: '))

print('=*=' * 20)
# Solicita ao usuário que escolha a base de conversão (binário, octal ou hexadecimal).
base = int(input("Escolha a base de conversão."
                 "\n \033[35m[1]\033[m para binário "
                 "\n \033[35m[2]\033[m para octal "
                 "\n \033[35m[3]\033[m para hexadecimal: "))
print('=*=' * 20)

# Converte o valor para binário, octal e hexadecimal. [2:] Exclui, Fatia os dois primeiros dígitos.
binario = bin(base_numerica)[2:]
octal = oct(base_numerica)[2:]
hexadecimal = hex(base_numerica)[2:]

# Verifica qual base de conversão foi escolhida e imprime o resultado correspondente.
if base == 1:
   print(f'O número \033[33m{base_numerica}\033[m, convertido para binário é: \033[2:33m{binario}\033[m')

elif base == 2:
   print(f'O número \033[33m{base_numerica}\033[m, convertido para octal é: \033[2:33m{octal}\033[m')

elif base == 3:
   print(f'O número \033[33m{base_numerica}\033[m, convertido para hexadecimal é: \033[2:33m{hexadecimal}\033[m')

else:
   # Se uma base inválida for escolhida, imprime uma mensagem de erro.
   print('\033[2:31m Base inválida\033[m. Escolha '
         '(\033[2:35m[1]\033[m para binário, '
         '\033[2:35m[2]\033[m para octal, '
         '\033[2:35m[3]\033[m para hexadecimal): '
         f' \n [{"-*-" * 10}\033[2:31m ATUALIZE A PÁGINA \033[m{"-*-" * 10}] ')

print('')
print(f'{"+-+" * 11}\033[4:36m FIM DA EXECUÇÃO\033[m {"+-+" * 11} ')
