# Leitura dos valores de dias, horas, minutos e segundos
dias = int(input("Digite a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

total1 = dias * 24 * 60 * 60
total2 = horas * 60 * 60 
total3 = minutos * 60 
total4 = total1 + total2 + total3 + segundos

print("O total é: %d segundos" % total4)
