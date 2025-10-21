# Punto 1
# Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

try:
    num = int(input("Ingresá un número: "))
    if es_primo(num):
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
except ValueError:
    print("Por favor, ingresá un número entero válido.")
