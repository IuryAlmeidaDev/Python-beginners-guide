#Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input("Qual é a distancia a percorrer? "))
velocidade_media = int(input("Qual a velocidade média esperada pra viagem ? "))


tempo_viagem = distancia / velocidade_media

print("O tempo estimado de viagem é de %2.2f horas." % tempo_viagem)
