from datetime import date
print(f'{'**' * 10}[CATEGORIA DOS ATLETAS]{'**' * 10}')


ano = date.today().year
idade = int(input('Digite sua idade: '))
ano_nas = ano - idade

print(f'{'=='*10}[INFORMAÇÕES DO PARTICIPANTE]{'=='*10}')
print(f'Você nasceu no ano de {ano_nas}. \n'
      f'Você tem {idade} anos.')

print(f'{'=='*10}[SUA CATEGORIA]{'=='*10}')
if idade <= 9:
   print(f'Categoria: MIRIM.')
elif idade <= 14:
   print(f'Categoria é INFANTIL.')
elif idade <= 19:
   print(f'Categoria é JÚNIOR.')
elif idade <= 25:
   print(f'Categoria é SÊNIOR.')
else:
   print(f'Categoria é MASTER.')


