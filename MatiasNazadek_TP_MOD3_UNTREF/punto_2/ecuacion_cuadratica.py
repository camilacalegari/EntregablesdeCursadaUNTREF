# Este código fue hecho por Matias Nazadek.

# Función que dado el ingreso de 3 variables (a, b, c) retorna las raíces resultantes de una ecuación cuadrática.
# La variable 'a' no puede ser 0, esto decidí validarlo con un if apenas el usuario ingresa el número.

import math

def formula_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante < 0:
        return "No tiene raíces reales"

    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2

a = float(input("Ingresá a: "))

if a == 0:
    print("'a' no puede ser 0.")
else:
    b = float(input("Ingresá b: "))
    c = float(input("Ingresá c: "))

    resultado = formula_cuadratica(a, b, c)
    print("Resultado:", resultado)
