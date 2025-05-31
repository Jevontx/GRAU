soma = 0
numero = 1

while numero != 0:
    numero = int(input("Digite um número a ser somado: "))

    soma = soma + numero
    print(soma)
    
    if numero == 0:
        print(f"A soma total é de: {soma}")