# Solicita os valores iniciais ao usuário
divida_inicial = float(input("Digite o valor inicial da dívida: "))
taxa_juros = float(input("Digite o valor da taxa de juros mensal (em %): "))
pagamento_mensal = float(input("Digite o valor que será pago mensalmente: "))

# Inicializa as variáveis
meses = 0
divida_atual = divida_inicial
total_pago = 0
total_juros = 0

# Loop para calcular o pagamento mês a mês
while divida_atual > 0:
    # Calcula os juros do mês
    juros_mes = (taxa_juros * divida_atual) / 100
    
    # Atualiza a dívida com os juros
    divida_atual += juros_mes
    
    # Verifica se o pagamento do mês é maior que a dívida atual
    if pagamento_mensal > divida_atual:
        pagamento_mensal = divida_atual  # Se sim, paga o restante da dívida
    
    # Subtrai o pagamento mensal da dívida
    divida_atual -= pagamento_mensal
    
    # Acumula o total pago e os juros pagos
    total_pago += pagamento_mensal
    total_juros += juros_mes
    
    # Incrementa o contador de meses
    meses += 1

# Exibe os resultados
print(f"Número de meses para pagar a dívida: {meses}")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pago: R${total_juros:.2f}")
