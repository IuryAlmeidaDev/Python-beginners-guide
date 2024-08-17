# Faça um prrograma para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10,9,8.... até 0


contagem = 11

while contagem >= 1:
    contagem -= 1
    print(contagem)

    if contagem == 0:
        print("E FOGO!")