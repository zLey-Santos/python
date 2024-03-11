nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print(f'Olá, muito prazer em te conhecer: {nome}! \n'
      f'O seu primeiro nome é: {n[0]} \n'
      f'O seu ultimo nome é: {n[len(n)-1]}')
