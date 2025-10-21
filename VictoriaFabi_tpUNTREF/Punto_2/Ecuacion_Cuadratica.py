# Escribir una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces resultantes de una ecuación cuadrática.


def calcular_cuadratica(a, b, c):
    """Esta función calcula las raíces de una ecuación cuadrática ax^2 + bx + c = 0.
    Retorna una tupla con las raíces si existen, None si no hay raíces reales, o un mensaje si a es 0."""
    if a == 0:
        return "No es una ecuación cuadrática"

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + discriminante**0.5) / (2*a)
        raiz2 = (-b - discriminante**0.5) / (2*a)
        return (raiz1, raiz2)
    elif discriminante == 0:
        raiz = -b / (2*a)
        return (raiz,)
    else:
        return None


#*******************ejemplo de uso*******************
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

resultado = calcular_cuadratica(a, b, c)

if resultado == "No es una ecuación cuadrática":
    print(resultado)
elif resultado is None:
    print("La ecuación no tiene raíces reales.")
elif len(resultado) == 1:
    print(f"La ecuación tiene una raíz real: {resultado[0]}")
else:
    print(f"La ecuación tiene dos raíces reales: {resultado[0]} y {resultado[1]}")

        