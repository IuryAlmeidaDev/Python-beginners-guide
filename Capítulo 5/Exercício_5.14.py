# Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução,
# exiba a quantidade de números digitados, assim como a soma e a média aritmética.

contador = 0

soma = 0

while True:
    numeros = int(input("Digite algum numero: "))
    soma += numeros
    contador += 1
    media = soma / contador

    if numeros == 0:
            print(f"A quantidade de numeros que foi digitados {contador}")
            print(f"A soma total dos numeros digitados é de {soma}")
            print(f"a media total dos numero digitados foi de {media}")
        
            break
