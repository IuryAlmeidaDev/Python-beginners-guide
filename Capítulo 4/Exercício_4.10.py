# Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir

kwh = int(input("Qual a quantidade de kWh consumida? "))
instalaçao = input("qual o tipo de instalaçao? R para residencias, I para industrias e C para comercios: ")

if instalaçao == "R" and kwh <= 500:
    total = kwh * 0.40
elif instalaçao == "R" and kwh > 500:
    total = kwh * 0.65
elif instalaçao == "C" and kwh <= 1000:
    total = kwh * 0.55
elif instalaçao == "C" and kwh > 1000:
    total = kwh * 0.60
elif instalaçao == "I" and kwh <= 5000:
    total = kwh * 0.55
elif instalaçao == "I" and kwh > 5000:
    total = kwh * 0.60
else:  
    print("voce nao digitou as informaçoes adequadamente")

print(f"O valor total a ser pago será de {total:.2f}")