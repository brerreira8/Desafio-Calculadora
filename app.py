# Importa a biblioteca 'random' para gerar números aleatórios
import random

# Gera um número aleatório entre 1 e 10
numero_secreto = random.randint(1, 10)

# Exibe uma mensagem inicial
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

# Pede ao usuário para digitar um número
palpite = int(input("Digite seu palpite: "))

# Verifica se o palpite está correto
if palpite == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! O número era", numero_secreto)
