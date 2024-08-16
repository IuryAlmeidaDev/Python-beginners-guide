#Faça um programa que calcule o aumento de um alário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumneto e do novo salário.

salario = int(input("Digite o seu salario autal: "))
aumento = int(input("Qual foi a porcentagem do aumento do seu salario? "))

aumento_real = salario * aumento /100
novo_salario = salario +(salario * aumento /100)

print("O aumento do salario foi de %d reais" % aumento_real)
print("O valor do novo salario é de: %d reais" %novo_salario)