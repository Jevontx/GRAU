numero = int

while numero != 0:
    
    print("->> Cardápio <<-")
    print("1 - Hambúrguer")
    print("2 - Pizza")
    print("3 - Refrigerante")
    print("4 - Iogurte")
    print("5 - Microfone")
    print("0 - Sair")

    numero = int(input("Digite sua opção: "))
    
    if numero == 1:
        print("Você escolheu Hambúrguer")

    if numero == 2:
        print("Você escolheu Pizza")

    if numero == 3:
        print("Você escolheu Refrigerante")

    if numero == 4:
        print("Você escolheu Iogurte")

    if numero == 5:
        print("Você escolheu Microfone")

    elif numero == 0:
        print("Saia do meu restaurante agora!!!")
        break

    else:
        print("Opção inválida")

    