# >>Criando game de advinhação<<
import os

print("Bem vindo ao jogo do número secreto!")
print(">>Instruções<<")
print("Defina um número secreto para seu amigo(a) tentar advinhar")
print("Após isso, dê um clear no visual para que ele não veja o número que você escolheu")

secret_number = int(input("Digite um número para ser o número secreto: "))
os.system('cls')

tentativas = 0
contagem_tentativas = 0

while tentativas != secret_number:
    numero = int(input("Digite a sua tentativa: "))
    contagem_tentativas = contagem_tentativas + 1

    if numero == secret_number:
        print("Você acertou!!")
        print(f"Você precisou de {contagem_tentativas} tentativas para acertar")
        break

    elif numero < secret_number:
        print("Dica: O número é maior que o número digitado")

    else:
        print("Dica: O número digitado é menor que o número digitado")
  

                 




