print("**********************************")
print("Bem vindo no jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    #O .format unido a string faz com que os elementos no parenteses sejam realocados no sitring
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    # o input sempre pega uma string, por isso devemos mudar para um número
    chute = int(input("Digite o seu numero: "))
    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
    rodada = rodada + 1
print("Fim do jogo!!")