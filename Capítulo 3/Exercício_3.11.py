# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preço = int(input("Digite o valor da mercadoria: "))
desconto = int(input("Digite o desconto do produto: "))

desconto_total = preço * desconto /100
valor_total = preço - desconto_total

print("O valor do desconto é de %d reais" % desconto_total)
print("O valor total a pagar é de %d" %valor_total)