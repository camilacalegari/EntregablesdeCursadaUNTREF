import math
#Este codigo es de Damian Rodriguez
def ecuacion_cuadratica(a, b, c):
    
    #escribir una funcion que dado el ingreso de 3 variables (a,b,c) retorne las raices de una ecuacion cuadratica utilizar la siguiente formula : x = -b +- RC(b**2 -4.a.b.c)/2.a
    
    # Verificar si es realmente una ecuación cuadrática
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero. No es una ecuación cuadrática.")
    
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    
    if discriminante >= 0:
        
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2
    else:
        
        return "No hay soluciones reales (discriminante negativo)"

def main():
    print("Resolver ecuación cuadrática ax² + bx + c = 0")
    try:
        # Pedimos los valores con inputs hace referencia a esto de la consigna (ingreso de 3 variables)
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        
        resultados = ecuacion_cuadratica(a, b, c)
        
        if isinstance(resultados, tuple):
            print(f"\nLas soluciones son:")
            print(f"x1 = {resultados[0]}")
            print(f"x2 = {resultados[1]}")
        else:
            print(f"\n{resultados}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
