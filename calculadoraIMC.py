print(" Bem vindo a calculadora de IMC!")
altura = float(input("Para começar digite a sua altura em metros:"))
peso = int(input("Agora digite seu peso:"))
IMC = round((peso/(altura*altura)),2)
IMC = str(IMC)
print("Seu IMC é: " + IMC)

IMCVerificado = float(IMC)

if IMCVerificado < 18.50:
  print("Você está abaixo do peso ideal")
elif IMCVerificado >= 18.60 and IMCVerificado <= 24.90:
  print("Você está no peso ideal")
elif IMCVerificado >= 25.0 and IMCVerificado <= 29.90:
  print("Você está levemente acima do peso")
elif IMCVerificado >= 30.0 and IMCVerificado <= 34.90:
  print("Você está com Obesidade Grau I")
elif IMCVerificado >= 35.0 and IMCVerificado <= 39.90:
  print("Você está com Obesidade Grau II")
elif IMCVerificado >= 18.60 and IMCVerificado <= 24.90:
  print("Você está com Obesidade Grau III")
else:
  "Tente novamente"