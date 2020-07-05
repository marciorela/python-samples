import random

chances = 7
chutes = 0
acertou = False
numero = random.randint(1, 100)

while chutes < chances and not acertou:
    chutes = chutes + 1
    chute = int(input('Tentativa %d: Informe o número: ' % chutes))

    if chute == numero:
        print('PARABÉNS!!! Você acertou com %d tentativas!!' % chutes)
        acertou = True

    elif chute > numero:
        print('O número informado é MAIOR que o número escolhido.')

    else:
        print('O número informado é MENOR que o número escolhido.')

if not acertou:
    print('O número escolhido foi %d.' % numero)
