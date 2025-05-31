# 1 - Solicitar as entradas de dados como: Nome, Peso e altura.
# 2 - IMC = Peso / (altura*altura)
# Exibir os dados e recomendações

# Declarando Variávies e Solicitando Entrada de Dados

nome = str(input("Qual o nome do paciente? : "))
idade = int(input("Qual a idade do paciente? : "))
peso = float(input("Qual o peso atual do paciente? : "))
altura = float(input("Qual a altura do paciente em questão? : "))


imc = peso / (altura*altura)

print(f"O IMC do paciente {nome} é de {imc} ! ")

if (imc < 18.5):
    print("O paciente está abaixo do peso! ")

elif 18.6 <= imc <= 24.9:
    print("O paciente está em seu peso normal! ")

elif 25 <= imc <= 29.9:
    print("O paciente está em sobrepeso! ")

else:
    print("O paciente está em estado de obesidade! ")


print("----- Ficha técnica do paciente -----")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Peso: {peso}")
print(f"Altura : {altura}")