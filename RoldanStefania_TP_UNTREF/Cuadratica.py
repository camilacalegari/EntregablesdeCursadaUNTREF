import math

def calcular_raices(a, b, c):
    # Calculamos el discriminante (lo que está dentro de la raíz)
    discriminante = b**2 - 4*a*c

    # Si el discriminante es positivo → dos raíces reales
    if discriminante > 0:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Las raíces son reales y distintas: x1 = {x1}, x2 = {x2}"

    # Si el discriminante es 0 → una raíz real doble
    elif discriminante == 0:
        x = -b / (2 * a)
        return f"Las raíces son reales e iguales: x = {x}"

    # Si el discriminante es negativo → raíces complejas
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
        return f"Las raíces son complejas: x1 = {parte_real} + {parte_imaginaria}i, x2 = {parte_real} - {parte_imaginaria}i"

# Programa principal
a = float(input("Ingresá el valor de a: "))
b = float(input("Ingresá el valor de b: "))
c = float(input("Ingresá el valor de c: "))

resultado = calcular_raices(a, b, c)
print(resultado)
