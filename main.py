from usuario_a import fibonacci, capicua, numero_perfecto
from usuario_b import primos_en_rango, es_primo, factorial, mcd


def mostrar_menu():
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Serie Fibonacci")
    print("2. Número Capicúa")
    print("3. Número Perfecto")
    print("4. Números Primos en un Rango")
    print("5. Verificar si un Número es Primo")
    print("6. Factorial")
    print("7. Máximo Común Divisor (MCD)")
    print("8. Salir")
    print("==================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese la cantidad de términos: "))
            fibonacci(n)

        elif opcion == "2":
            numero = input("Ingrese un número: ")
            capicua(numero)

        elif opcion == "3":
            numero = int(input("Ingrese un número: "))
            numero_perfecto(numero)

        elif opcion == "4":
            inicio = int(input("Ingrese el valor inicial: "))
            fin = int(input("Ingrese el valor final: "))
            primos_en_rango(inicio, fin)

        elif opcion == "5":
            numero = int(input("Ingrese un número: "))
            es_primo(numero)

        elif opcion == "6":
            n = int(input("Ingrese un número: "))
            factorial(n)

        elif opcion == "7":
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            mcd(a, b)

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()




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
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma == numero
numero = int(input("Ingrese un numero: "))

if es_perfecto(numero):
    print("Es numero perfecto")
else:
    print("No es numero perfecto")