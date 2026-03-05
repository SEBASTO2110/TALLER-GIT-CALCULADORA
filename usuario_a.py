def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b




def es_capicua(numero):
    if str(numero) == str(numero)[::-1]:
        print("Es capicua")
    else:
        print("No es capicua")



def es_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
        return suma == numero
    if suma == numero:
        print("Es numero perfecto")
    else:
        print("No es numero perfecto")
