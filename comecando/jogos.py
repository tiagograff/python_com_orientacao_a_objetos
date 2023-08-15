import forca
import adivinhacao

print('escolha o seu jogo')
print('(1) forca | (2) adivinhacao')

jogo = int(input('qual jogo? '))
if (jogo == 1):
    print('jogando o jogo da forca')
    forca.jogar()
elif (jogo == 2):
    print('jogando o jogo de adivinhacao')
    adivinhacao.jogar()
