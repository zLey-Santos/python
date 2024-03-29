
s, ct = 0, 0
for c in range(1, 6 + 1):
  n = int(input(f'Digite o {c}º valor: '))
  if n % 2 == 0:
    s += n 
    ct += 1
print(f'Você digitou {ct} números PARES e a soma entre eles é igual a {s}.')  
