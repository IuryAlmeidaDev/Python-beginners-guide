#Escreva um programa que converta uma temperatura digitada em celsius PARA fahrenheit. A formula de conversao é f = 9 x C / 5 +32


temperatura = int(input("Digite a temperatura atual: "))

print ("Essa é a temperatura atual em graus celsius: %d" %temperatura)

fahrenheit = (temperatura * 9 / 5) +32

print("Essa é a temperatura atual em Fahrenheit: %.2f" % fahrenheit)
