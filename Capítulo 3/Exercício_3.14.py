# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

km_percorrido = int(input("Qual foi a quantidade de KM percorrido? "))
dias_alugado = int(input("Qual foi a quantidade de dias que o carro foi alugado? "))

valor_total = (km_percorrido * 0.15) + (dias_alugado * 60)

print(f"O valor total a pagar das custas do veiculo é de {valor_total} reais")