# Versão CEV Melhor versão 2
# Solicita ao usuário que informe seu sexo e armazena a entrada convertida para maiúsculas e sem espaços em branco,
# pegando apenas o primeiro caractere. (.strip().upper()[0])
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

# Enquanto a entrada do sexo não estiver entre 'M', 'm', 'F' ou 'f', continua pedindo ao usuário para fornecer uma entrada válida.
while sexo not in 'MmFf':
    sexo = str(input("Opção Inválida, tente novamente, informe seu sexo: [M/F] ")).strip().upper()[0]
# Quando uma entrada válida for fornecida, exibe uma mensagem confirmando o sexo registrado e encerra o loop.
print(f'Sexo \033[31m[{sexo}]\033[m registrado com sucesso!')
print('fim')


'''
PIOR VERSÂO
sf = 'F'
sm = 'M'
sexo = str(input("Informe seu sexo: [M/F] ")).strip().upper()[0] 
while sf and sm :  
  sexo = str(input("Opção Inválida, tente novamente, informe seu sexo: [M/F] ")).strip().upper()[0] 
  if sexo == 'F':
    print(f'Sexo {sf}, Femenino registrado com sucesso!')
  elif sexo == 'M':
    print(f'Sexo {sm}, Masculino registrado com sucesso!')
    '''
 

