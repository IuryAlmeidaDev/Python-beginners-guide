# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuario. Cálcule o total em segundos.

dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantida de seegundos: "))

total1 = dias * 24
total2 = (horas + total1) *60
total3 = (minutos + total2) *60
total4 = total3 + segundos

print("o total é:  %d"  %total4)

