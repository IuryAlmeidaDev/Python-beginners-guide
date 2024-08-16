# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesso caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h


velocidade = int(input("Qual a velocidade do carro? "))


if velocidade <= 80:
    print("voce nao foi multado")
else:
    multa = (velocidade - 80)*5
    print ("voce foi multado em %d reais" % multa)