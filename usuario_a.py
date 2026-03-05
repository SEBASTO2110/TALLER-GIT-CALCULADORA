def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b

n = int(input("Ingrese la cantidad de términos: "))
fibonacci(n)


def es_capicua(numero):
    texto = str(numero)
    return texto == texto[::-1]
numero = int(input("Ingrese un numero: "))

if es_capicua(numero):
        print("Es capicua")
else:
        print("No es capicua")


def es_perfecto(numero):
    pass