#Exercício 5.15 Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade
#comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto:
total = 0
while True:
    codigo = float(input("Digite o codigo do produto: "))

    if codigo == 1:
        preço = 0.50
    elif codigo == 2:
        preço = 1.00
    elif codigo == 3:
        preço = 4.00
    elif codigo == 5:
        preço = 7.00
    elif codigo == 9:
        preço = 8.00
    elif codigo == 0:
        break
    else:
        print("Voce digitou algo errado!")
        
    
    quantidade = int(input("Digite a quantidade de produtos: "))
    total += quantidade * preço

print (f"O total da sua compra é de apenas: {total:2.2f} reais")


