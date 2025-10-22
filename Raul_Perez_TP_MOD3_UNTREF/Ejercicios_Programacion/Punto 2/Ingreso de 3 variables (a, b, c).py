import cmath

def calcular_raices(a, b, c):
  
    if a == 0:
        raise ValueError("El valor de 'a' no puede ser cero. No es una ecuación cuadrática.")

    discriminante = b**2 - 4*a*c

    x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
    x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)

    return x1, x2

try:
    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    c = float(input("Ingresa el valor de c: "))

    raices = calcular_raices(a, b, c)
    print(f"Las raíces son: x1 = {raices[0]}, x2 = {raices[1]}")

except ValueError as error:
    print(f"Error: {error}")

