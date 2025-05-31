# - Sistema de padaria

opcao = -1
resultado1 = 0
resultado2 = 0
resultado3 = 0
resultado4 = 0
resultado5 = 0

while opcao != 0:

    print("->>> PADARIA DOS INFERNOS <<<-")
    print("1 - Pão Demoniaco - R$ 1.04")
    print("2 - Pão Asa Negra - R$ 1.04")
    print("3 - Pão Magia - R$ 1.08")
    print("4 - Pão Serberus - R$ 6.66")
    print("5 - Pão que o diabo não conseguiu amassar - R$ 9.99")
    print("0 - Sair")

    opcao = int(input("Faça sua escolha: "))

    if opcao == 1:
        print("Você escolheu Pão Demoníaco por R$ 1.04")
        qtd=int(input("Digite a quantidade de pães desejados: "))
        resultado1 = qtd * 1.04
        print(f"O total de {qtd} Pães Demoníaco é de: R$ {resultado1:.2f}")

    elif opcao == 2:
        print("Você escolheu Pão Asa Negra por R$ 1.04")
        qtd=int(input("Digite a quantidade de pães desejados: "))
        resultado2 = qtd * 1.04
        print(f"O total de {qtd} Pães Asa Negra é de: R$ {resultado2:.2f}")

    elif opcao == 3:
        print("Você escolheu Pão Magia por R$ 1.08")
        qtd=int(input("Digite a quantidade de pães desejados: "))
        resultado3 = qtd * 1.08
        print(f"O total de {qtd} Pães Magia é de: R$ {resultado3:.2f}")

    elif opcao == 4:
        print("Você escolheu Pão Serberus por R$ 6.66")
        qtd=int(input("Digite a quantidade de pães desejados: "))
        resultado4 = qtd * 6.66
        print(f"O total de {qtd} Pães Serberus é de: R$ {resultado4:.2f}")

    elif opcao == 5:
        print("Você escolheu que o diabo não conseguiu amassar por R$ 9.99")
        qtd=int(input("Digite a quantidade de pães desejados: "))
        resultado5 = qtd * 9.99
        print(f"O total de {qtd} Pães que o diabo não conseguiu amassar é de: R$ {resultado5:.2f}")

    elif opcao == 0:
        print("Você saiu!")
        resultadofinal = resultado1 + resultado2 + resultado3 + resultado4 + resultado5
        print(f"O total a ser pago é de: R$ {resultadofinal:.2f}")
        break

    else:
        print("Por gentileza, escolha uma opção válida '-'")