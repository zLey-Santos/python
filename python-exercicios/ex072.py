numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
            "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete",
              "dezoito", "dezenove", "vinte")

respostas = ("sim", "não")

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        print(f"Você digitou o número {numeros[num]}")
    else:
        print("Número inválido. Tente novamente.")
    
    while True:
        resposta = input("Deseja continuar? (sim/não): ").lower()
        if resposta in respostas:
            if resposta == "não":
                print('Fim Da Execução!')
                exit()
              
            else:
                break
        else:
            print("Resposta inválida. Tente novamente.")
              
       
   