# Importação de ferramentas
import random

#declaração de variáveis
numero_secreto = random.randint(1, 100)
tentativas = 0

# Algoritmo de adivinhação
while True:
    palpite = int(input('Adivinhe o número secreto (entre 1 e 100): '))
    tentativas += 1

    if palpite == numero_secreto:
        print(f'Parabéns! Você acertou o número em {tentativas} tentativas.')
        break
    elif palpite < numero_secreto:
        print('Tente um número maior.')
    else:
        print('Tente um número menor.')