# Solicita a entrada de dois números inteiros
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opcao = 0

# Loop principal que continua até a opção 5 (sair do programa) ser escolhida
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
    
    # Solicita a entrada da opção desejada
    opcao = int(input('Digite a opção desejada: '))
    
    # Verifica a opção escolhida e executa a operação correspondente
    if opcao == 1:
        # Calcula a soma dos números
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a {soma}') 
    
    elif opcao == 2:  
        # Calcula o produto dos números
        mult = n1 * n2   
        print(f'A multiplicação entre {n1} e {n2} é igual a {mult}')
    
    elif opcao == 3:
        # Verifica qual número é maior ou se são iguais
        if n1 > n2:
            maior = n1
            print(f'O maior número é {maior}')
        elif n1 < n2:
            maior = n2
            print(f'O maior número é {maior}')
        else:
            print('Os dois números são iguais!')
    
    elif opcao == 4:
        # Permite a entrada de novos números
        n1 = int(input('Digite o primeiro novo número: '))
        n2 = int(input('Digite o segundo novo número: '))
        
# Mensagem de encerramento do programa
print('Fim do programa. Volte sempre!')
