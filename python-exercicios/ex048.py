s, ct = 0, 0

for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        s += c
        ct = ct + 1
print(f'A soma de todos os {ct} valores é igual a: {s}')
