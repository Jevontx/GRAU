# Locadora de carro

print("___________________________________")
print("|         ->>> Tabela <<<-        |")
print("| Valor por dia alugado: R$ 90.00 |")
print("| Valor por Kms rodados: R$ 0.20  |")
print("|---------------------------------|")
print("|     Carro alugado: KWID         |")
print("|---------------------------------|")

dias = float(input("Digite a quantidade de dias que você ficou com o carro: "))
kms = float(input("Digite a quantidade de Kms rodados: "))
resultado = (dias * 90.00) + (kms * 0.20)

print(f"O total a ser pago é de: R$ {resultado:.2f}")






