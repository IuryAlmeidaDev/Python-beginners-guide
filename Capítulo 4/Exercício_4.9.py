# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade
# de anos a pagar. O valor da prestação mensal nao pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Qual o valor da casa que voce deseja comprar? "))
salario = float(input("Qual seu salario atual? "))
anos = float(input("Em quantos anos que deseja parcelar? "))

tempo = anos * 12
valor_mensal = valor_casa / tempo

limite = salario - (salario * 70 / 100)

if valor_mensal > limite :
    print("Voce nao pode comprar a casa pois a parcela ultrapassa 30 por cento do seu salário, que pena! ")
else: 
    print(f"O valor da sua parcela será {valor_mensal:.2f} reais, parábens")