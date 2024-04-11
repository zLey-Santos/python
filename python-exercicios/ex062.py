print('Gerador de PA')
print('=' * 20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
tot = 0
mais = 10

while mais !=0: 
    tot += mais

    while cont <= tot:
      print(f'{termo}', end=' -> ' )
      termo += razao
      cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'PA Finalizada com {tot} termos realizados!')
