# - Transformando Temperaturas -

print("<<<- Instruções ->>>")
print("Primeiro faça sua escolha")
print("Segundo, digite a temperatura em Celcius, Kelvin ou Fahrenheit.")
print("Terceiro, resultado na tela :)")

temp1 = float
resultado = float
opcao = -1



while opcao != 0:

    print("1 - Celcius para Kelvin")
    print("2 - Celcius para Fahrenheit")
    print("3 - Kelvin para Celcius")
    print("4 - Fahrenheit para Celcius")
    print("0 - Sair :(")

    opcao = int(input("Faça sua escolha: "))

    if opcao == 1:
        print("Você escolheu Celcius para Kelvin")
        temp1=float(input("Digite a temperatura em Celcius: "))
        resultado = temp1 + 273.15
        print(f"O resultado da transformação em é de: {resultado} °K")

    elif opcao == 2:
        print("Você escolheu Celcius para Fahrenheit")
        temp1=float(input("Digite a temperatura em Celcius: "))
        resultado = (temp1 * 9 / 5) + 32
        print(f"O resultado da transformação é de: {resultado} °F")

    elif opcao == 3:
        print("Você escolheu Kelvin para Celcius")
        temp1=float(input("Digite a temperatura em Kelvin: "))
        resultado = temp1 - 273.15
        print(f"O resultado da transformação é de: {resultado} °C")

    elif opcao == 4:
        print("Você escolheu Fahrenheit para Celcius")
        temp1=float(input("Digite a temperatura em Fahrenheit: "))
        resultado = (temp1 - 32) / 1.8
        print(f"O resultado da transformação é de: {resultado} °C")

    else:
        print("Opção inválida!!")
        print("Meu fi, cê tem que escolher uma parada válida.")
        print(">:(")
        break
        



