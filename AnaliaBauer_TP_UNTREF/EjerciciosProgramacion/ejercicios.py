import math

#Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no. 
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Ejecucion del programa
num = int(input("Ingrese un número: "))
if es_primo(num):
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")
    
#Escribir una función que dado el ingreso de 3 variables (a, b, c) retorne las raíces 
#resultantes de una ecuación cuadrática.

def resolver_ecuacion_cuadratica(a, b, c):
    # Calculamos el discriminante
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        # Dos raíces reales distintas
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Raíces reales distintas: x1 = {x1:.2f}, x2 = {x2:.2f}"
    elif discriminante == 0:
        # Una raíz real doble
        x = -b / (2 * a)
        return f"Raíz doble: x = {x:.2f}"
    else:
        # Raíces complejas
        parte_real = -b / (2 * a)
        parte_imaginaria = math.sqrt(-discriminante) / (2 * a)
        return f"Raíces complejas: x1 = {parte_real:.2f} + {parte_imaginaria:.2f}i, x2 = {parte_real:.2f} - {parte_imaginaria:.2f}i"


# Ejecucion del programa
if __name__ == "__main__":
    print("Ecuación cuadrática: ax² + bx + c = 0")
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))

    resultado = resolver_ecuacion_cuadratica(a, b, c)
    print(resultado)


    