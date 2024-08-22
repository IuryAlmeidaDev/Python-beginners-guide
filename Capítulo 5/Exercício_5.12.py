valor_inicial = int(input("Digite o valor inicial do deposito: "))
taxa_de_juros = int(input("Digite o valor da taxa de juros: "))
valor_mensal = float(input("Digite o valor que será depositado todo mês: "))

mes = 1

saldo = valor_inicial

acumulador = 0


while mes <= 24:
    saldo += valor_mensal
    juros_mes = (taxa_de_juros * saldo) /100
    saldo += juros_mes
    acumulador += juros_mes
    print(f"Mês {mes}: Juros = R${juros_mes:.2f}, Saldo = R${saldo:.2f}")
    mes += 1

print(f"Total ganho com juros após 24 meses: R${acumulador:.2f}")