import random

print("bem vindo ao jogo de adivinhacao")

numero_secreto = random.randint(0, 101)
tentativa = 0
rodada = 0
pontos = 1000

print('qual o nível de dificuldade você deseja?')
print('(1) fácil | (2) normal | (3) difícil')
nivel = int(input('definir o nível: '))

if (nivel == 1):
    tentativa = 10
elif (nivel == 2):
    tentativa = 6
else:
    tentativa = 3

for rodada in range(1, tentativa + 1):
    print("tentativa: {} de {}".format(rodada, tentativa))

    chute = int(input("digite um numero entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("voce deve digitar um numero entre 1 e 100")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("voce acertou, e vez {} pontos".format(pontos))
        break
    else:
        if maior:
            print("errou o seu numero foi maior que o numero secreto.")
            if (rodada == tentativa):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))
        elif menor:
            print("errou o seu numero foi menor que o numero secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
            if (rodada == tentativa):
                print("O número secreto era {}. Você fez {}".format(
                    numero_secreto, pontos))

print("fim de jogo!")
