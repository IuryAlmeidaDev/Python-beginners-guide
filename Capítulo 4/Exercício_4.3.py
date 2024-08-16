# Escreva um programa que leia três números e que imprima o maior e o menos.
num1 = 1
num2 = 2
num3 = 3

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3
if num3 < menor:
    menor = num3

print("O maior número é:", maior)
print("O menor número é:", menor)