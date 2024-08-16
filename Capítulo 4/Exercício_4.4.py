#  Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00. Calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite o valor do seu salario: "))

aumento = 0
if salario > 1250:
    aumento = salario * 10 / 100
    print (f"Seu aumento foi de {aumento} reais")
else:
    salario <= 1250
    aumento = salario * 15 / 100
    print (f"Seu aumento foi de {aumento} reais")

