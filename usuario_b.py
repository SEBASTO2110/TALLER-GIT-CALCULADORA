def es_primo(n):
    if n < 2:
        return 
    for i in range(2, n):
            if n % i == 0:
                print("No es primo")
                return 
    print("Es primo")

def primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        primo = True
        if num < 2:
            primo = False
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break
        if primo:
            primos.append(num)
    print("Primos en el rango:", primos)

def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    print("El factorial es:", resultado)

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    print("El MCD es: ", a)