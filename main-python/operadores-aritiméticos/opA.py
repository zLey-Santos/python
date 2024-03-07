# Para números extensos, podemos formatar usando {valorVariável:.2f}. Por exemplo: 2,12345, a saída seria 2,12.
# /n quebra a linha
# end=' ' continua na mesma linha mesmo se tiver 2 prints()

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira: int = n1 // n2
exponenciacao = n1 ** n2
raiz_cubica = 3 * (n1 + n2) ** (1 / 3)

print(f'Os resultados dos valores {n1} e {n2} são:\n'
      f'Soma: {soma}\n'
      f'Multiplicação: {multiplicacao}\n'
      f'Divisão: {divisao:.3f}\n'
      f'Divisão Inteira: {divisao_inteira}\n'
      f'Exponenciação: {exponenciacao}\n'
      f'Ordem: {raiz_cubica:.3f}')

