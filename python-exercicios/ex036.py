# Solicita ao usuário o valor da casa, o salário do comprador e em quantos anos pretende pagar,
# e converte os valores para float.
valor_casa = float(input('Qual é o valor da casa? '))
valor_salario = float(input('Qual é o salário do comprador? '))
parcelas = float(input('Em quantos anos pretende pagar? '))

# Calcula o valor da parcela mensal dividindo o valor da casa pelo número total de parcelas (anos * 12).
casa = valor_casa / (parcelas * 12)
# Calcula o valor máximo permitido para as parcelas, que é 30% do salário do comprador.
salario = (valor_salario * 30) / 100

# Verifica se o valor da parcela mensal não excede 30% do salário do comprador.
if casa < salario:
   # Se o valor da parcela for menor ou igual a 30% do salário, o crédito é aprovado.
   print(f'Credito aprovado! \n'
         f'Valor da casa é R${valor_casa:.2f} e vai ser dividido por {parcelas:.0f} anos \n'
         f'O valor mensal das parcelas será de R${casa:.2f}')
else:
   # Se o valor da parcela exceder 30% do salário, o crédito é reprovado.
   print(f'Credito Reprovado! \n'
         f'O valor da casa é de R${valor_casa:.2f} dividido em {parcelas:.0f} anos \n'
         f'Excedeu o valor máximo de 30% do seu salário disponível para crédito, que é R${salario:.2f} \n'
         f'O valor das parcelas para {parcelas:.0f} anos é de R${casa:.2f}')

# Imprime uma linha de separação.
print('--' * 30)
# Imprime o nome da empresa.
print('***' * 10 + ' BANCO.sa COMPANY ' + '***' * 10)
