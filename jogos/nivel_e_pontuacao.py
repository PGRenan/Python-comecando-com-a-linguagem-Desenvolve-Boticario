import random
#random não é uma função built-in do python, logo é necessário importar esse modulo para poder ser usado

print("**********************************")
print("Bem vindo no jogo de adivinhação!")
print("**********************************")

#ja round é uma função built-in usado para arredondar um número, mas a função random gera um nuermo entrre 0.0 e 1.0 e 0 não é permitido pelo programa que estamos fazendo
#numero_secreto = round((random.random()*100))

#random.randrange é usado para criar um numero randomico, do numero inicial ao numero final -1
numero_secreto = round(random.randrange(1,101))
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")


nivel = int(input("Defina o nível: "))
if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    # O .format unido a string faz com que os elementos no parenteses sejam realocados no sitring
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # o input sempre pega uma string, por isso devemos mudar para um número
    chute = int(input("Digite o seu número entre 1 e 100: "))
    print("Você digitou ", chute)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
print("Fim do jogo!!")