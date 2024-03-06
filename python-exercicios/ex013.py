nome = input('Nome do funcionário: ')
salario = float(input(f'Qual o salario atual do {nome}: '))

reajuste = (salario * 15 / 100) + salario
imposto = reajuste * 11 / 100
sal_final = reajuste - imposto
print(f'O reajuste do funcionário {nome}  foi de 15% passando de R${salario:.2f} para R${reajuste:.2f} mensal. \n'
      f'Imposto pago ao estado do funcionário {nome} vai ser de 11% {imposto:.2f} \n'
      f'Sendo valor final de {sal_final:.2f}')

ret = imposto * 12
dev = ret - (ret * 15 / 100)
print('--IMPOSTO RETIDO A SER DEVOLVIDO--')
print(f'Valor retido é R${ret:.2f} e vai ser devolvido ao funcionário {nome} o valor de 85% R${dev:.2f}')