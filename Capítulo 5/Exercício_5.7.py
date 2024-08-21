# Modifique o programa anterior de forma q o usuario tambem digite o inicio e o fim da tabuada, em vez de começar com 1 e 10.

n = int(input(("Tabuada de: ")))
x = 1
while x <= 10:
    print(n*x)
    x=x+1