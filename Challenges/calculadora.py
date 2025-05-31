# Calculadora simples

opcao = -1

while opcao != 0:

    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair :(")

    opcao = int(input("Faça sua escolha: "))

    if opcao == 1:
        print("Você escolheu Somar")
        num1 = float(input("Digite o primeiro número a ser somado: "))
        num2 = float(input("Digite o segundo número a ser somado: "))
        resultado = num1 + num2
        print(f"O total é: {resultado}")

    elif opcao == 2:
        print("Você escolheu Subtrair")
        num1 = float(input("Digite o primeiro número para subtrair: "))
        num2 = float(input("Digite o segundo número para subtrair: "))
        resultado = num1 - num2
        print(f"O total é: {resultado}")

    elif opcao == 3:
        print("Você escolheu Multiplicar")
        num1 = float(input("Digite o primeiro número a ser multiplicado: "))
        num2 = float(input("Digite o segundo número a ser multiplicado: "))
        resultado = num1 * num2
        print(f"O total é: {resultado}")

    elif opcao == 4:
        print("Você escolheu Dividir")
        num1 = float(input("Digite o primeiro número a ser dividido: "))
        num2 = float(input("Digite o segundo número a ser dividido: "))
        resultado = num1 / num2
        print(f"O total é: {resultado}")

    elif opcao == 0:
        print("Você escolheu sair.")
        break

    else:
        print("Digite uma opção que seja válida!!!!")
