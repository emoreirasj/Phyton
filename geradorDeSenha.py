# importação de ferramentas
import random
import string

# Algoritmo gerador de senha
def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Coleta de dados para gerar a senha
comprimento = int(input('Digite o comprimento da senha desejada: '))
senha = gerar_senha(comprimento)

#Resposta
print(f'Sua senha gerada é: {senha}')