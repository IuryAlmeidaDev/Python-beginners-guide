# Escreva um programa para calcular a reduçao do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

quantidade_de_cigarros = int(input("Qual é a quantidade de cigarros que voce fuma por dia? "))
anos = int(input("quantos anos voce ja fumou? "))

total_cigarros = quantidade_de_cigarros * anos * 365

minutos_perdidos = total_cigarros * 10

dias_perdidos = minutos_perdidos / (60 * 24)

print(f"Voce perdera {dias_perdidos: .2f} dias de vida devido ao fumo.")
