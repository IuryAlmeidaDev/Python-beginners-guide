def calcular_total_compras():
    total = 0  # Variável para armazenar o total das compras

    while True:
        codigo = int(input("Digite o código do produto (ou 0 para finalizar): "))

        if codigo == 0:
            break  # Encerra o loop se o código for 0
        elif codigo == 1:
            preco = 0.50
        elif codigo == 2:
            preco = 1.00
        elif codigo == 3:
            preco = 4.00
        elif codigo == 5:
            preco = 7.00
        elif codigo == 9:
            preco = 8.00
        else:
            print("Código inválido")
            continue  # Volta para o início do loop se o código for inválido

        quantidade = int(input("Digite a quantidade comprada: "))
        total += preco * quantidade  # Calcula o total

    print(f"Total das compras: R$ {total:.2f}")

# Chama a função para executar o programa
calcular_total_compras()
