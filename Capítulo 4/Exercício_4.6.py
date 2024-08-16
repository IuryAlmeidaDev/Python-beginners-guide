# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
# Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até 200km, e R$ 0,45 para viagens mais longas

distancia = int(input("Qual distancia voce pretende percorrer em km? "))
total = 0
if distancia > 200:
    total = distancia * 0.45
    print (f"Voce vai gastar um total de {total} reais")
else :
    total = distancia * 0.50
    print (f"Voce vai gastar um total de {total:.2f} reais")

