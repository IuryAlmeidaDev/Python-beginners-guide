#Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

valor1 = int(input("Digite quantos metros tem sua rua: "))

centimetros = (valor1 * 100) 
milimetros = (centimetros * 10)

print ("Sua rua tem %d milimetros " % milimetros)