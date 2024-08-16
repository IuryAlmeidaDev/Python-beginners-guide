# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. Você deve poder calcular a soma (+)
# subtração  (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

operacao = input("Qual operação você deseja realizar? soma (+), subtração (-), multiplicação (*) ou divisão (/): ")

if operacao == "soma" or operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "subtracao" or operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "multiplicacao" or operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "divisao" or operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Tente novamente.")

