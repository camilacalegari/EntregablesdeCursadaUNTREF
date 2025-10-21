# Punto 2
# Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces resultantes de una ecuación cuadrática. 

import math

def resolver_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c
    print(f"Discriminante: {discriminante}")

    # Evaluamos el tipo de soluciones según el discriminante
    if discriminante > 0:
        print("El discriminante es positivo, hay 2 soluciones.")
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        print(f"X₁ = {x1}")
        print(f"X₂ = {x2}")
        return x1, x2

    elif discriminante == 0:
        print("El discriminante es 0, hay 1 solución.")
        x = -b / (2*a)
        print(f"X = {x}")
        return x

    else:
        print("El discriminante es negativo, no hay solucion.")
        return None

resolver_cuadratica(1, -3, 2)
resolver_cuadratica(1, -2, 1)
resolver_cuadratica(1, 4, 5)
