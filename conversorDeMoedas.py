# Algoritmo de conversão
def converter_moeda(valor, taxa):
    return valor * taxa

# Entrada do valor a ser convertido pelo usuário
valor = float(input('Digite o valor em sua moeda: '))

# Entrada do valor de cambio
taxa = float(input('Digite a taxa de câmbio: '))

# Chama a função para realizar a conversão e exibe o resultado
resultado = converter_moeda(valor, taxa)
print(f'O valor convertido é: {resultado}')