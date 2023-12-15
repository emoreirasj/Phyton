# Importação dos dados de data
from datetime import date

# Algorito de cálculo de idade
def calcular_idade(data_nascimento):
    hoje = date.today()
    ano_nascimento = data_nascimento.year
    idade = hoje.year - ano_nascimento
    if hoje.month < data_nascimento.month or (hoje.month == data_nascimento.month and hoje.day < data_nascimento.day):
        idade -= 1
    return idade

#coleta de dados de nascimento
ano_nascimento_user = int(input("Digite seu ano de nascimento:"))
mes_nascimento_user = int(input("Digite seu mês de nascimento:"))
data_nascimento_user = int(input("Digite o dia do seu nascimento:"))

# Organiza os dados coletados em uma variável de data
data_nascimento =date(ano_nascimento_user, mes_nascimento_user, data_nascimento_user)

# Chamada da função de cálculo de idade
idade = calcular_idade(data_nascimento)

# Retorno de resultado ao usuário
print(f'Sua idade é: {idade} anos')
