n1 = int(input('Digite um número: '))
n2  = int(input('Digite outro número: '))
opcao = 0

while opcao != 5:
 print()
 print(f'O que deseja fazer com os números {n1} e {n2}.')
 print('''
  [1] Somar 
  [2] Multiplicar 
  [3] Mostrar o Maior 
  [4] Novos números 
  [5] Sair do programa
  ''')
 opcao = int(input('Digite a opção desejada: '))
 if opcao == 1:
   soma = n1 + n2
   print(f'A soma entre {n1} e {n2} é igual a {soma}') 
 elif opcao == 2:  
   mult = n1 * n2   
   print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
 elif opcao == 3:
   if n1 > n2:
      maior = n1
      print(f'O maior número é {maior}')
   elif n1 < n2:
      maior = n2
      print(f'O maior número é  {maior}')
   else:
    print('Os dois números são iguais!')
 elif opcao == 4:
   n1 = int(input('Digite o primeiro novo números: '))
   n2 = int(input('Digite o segundo novo números: '))
   
print('Fim do programa. Volte sempre!')