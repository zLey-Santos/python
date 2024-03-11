frase = str(input('Digite uma frase: ')).upper().strip()

print(f'Sua frase {frase} contem {frase.count('A')} letras "A" \n' 
      f'A letra "A" aparece pela primeira vez na posição  {frase.find('A') + 1} \n'
      f'A ultima letra "A" apareceu na posição {frase.rfind('A') + 1} ')

