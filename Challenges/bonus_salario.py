nome=str(input("Você é o funcionário: "))
salario=float(input("Digite o seu salário fixo: R$ "))
vendas=int(input("Digite a quantidade de vendas feitas este mês: "))

if vendas >= 20:
    print(f"{nome}, você atingiu a meta de vendas, portanto, receberá um bonûs de 15%.")
    salarioBonus = salario * 0.15
    salarioFinal = salarioBonus + salario
    print(f"O seu salário com bonûs é de: R$ {salarioFinal}")

elif vendas < 20:
    print(f"{nome}, você não atingiu a meta, portanto, não haverá bônus.")


