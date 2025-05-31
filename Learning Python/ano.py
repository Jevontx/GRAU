ano = 2025
ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano - ano_nascimento

print(f"Sua idade é de: {idade}")

if idade < 18:
    print("Você não pode beber cerveja")

elif idade >= 18:
    print("Você pode beber cerveja")