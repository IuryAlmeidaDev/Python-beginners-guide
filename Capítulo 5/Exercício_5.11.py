valor_inicial = int(input("Digite o valor inicial do deposito: "))
taxa_de_juros = int(input("Digite o valor da taxa de juros: "))

mes = 1

saldo = valor_inicial

acumulador = 0

juros_mes = (taxa_de_juros * saldo) /100

while mes <= 24:
    juros_mes = (taxa_de_juros * saldo) /100
    saldo += juros_mes
    acumulador += juros_mes
    print(f"Mês {mes}: Juros = R${juros_mes:.2f}, Saldo = R${saldo:.2f}")
    mes += 1