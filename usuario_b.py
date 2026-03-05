def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
            if n % i == 0:
                return False
    return True

def primos_en_rango(inicio, fin):
    primos = []
    for num in range(inicio, fin + 1):
        if es_primo(num):
            primos.append(num) 
    return primos

def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def mcd(a, b):
    while b != 0:
        a, b = b, a % b