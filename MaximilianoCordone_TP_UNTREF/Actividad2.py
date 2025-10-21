""" 
Punto 2:
Escribir una función que, dado el ingreso de 3 variables (a, b, c), retorne las raíces
resultantes de una ecuación cuadrática. 
"""

def resol_cuadratica(a, b, c):    
    # Si 'a' es 0, no es una ecuación cuadrática
    if a == 0:
        print("Esto no es una ecuación cuadrática porque 'a' es 0.")
        return
    
    # Cálculo para discriminante
    discriminante = (b**2) - (4 * a * c)
    print(f"El valor del discriminante es: {discriminante}\n")
    
    # Si el discriminante es positivo, hay 2 soluciones
    if discriminante > 0:
        # Para la raíz cuadrada, usé ** 0.5
        raiz_discriminante = discriminante ** 0.5
        solucion1 = (-b + raiz_discriminante) / (2 * a)
        solucion2 = (-b - raiz_discriminante) / (2 * a)
        print(f"Hay 2 soluciones ya que el discriminante es mayor a 0.\n")
        print(f"La solución 1 es: {solucion1}\n")
        print(f"La solución 2 es: {solucion2}")
        
    # Si el discriminante es cero, hay 1 solución
    elif discriminante == 0:
        x = -b / (2 * a)
        print("Hay 1 solución ya que el discriminante es 0.\n")
        print(f"La solución (x) es: {x}")
        
    # Si el discriminante es negativo, no hay solución
    else: # Esto cubre el caso de discriminante < 0
        print("El discriminante da negativo, no hay soluciones reales.\n")
        

def iniciar_programa():
    while True:
        try:
            dato = input('\nBienvenido a la solución de ecuaciones cuadráticas.\nDesea continuar con el programa? (S/N)')
            
            if (dato.lower() =='n'):
                print("Chau!")
                break
            
            elif (dato.lower() =='s'):
                a = int(input("Ingrese el valor de 'a': "))
                b = int(input("Ingrese el valor de 'b': "))
                c = int(input("Ingrese el valor de 'c': "))
                resol_cuadratica(a, b, c)
                
            else:
                print("\nLa entrada ingresada no es válida, intenta nuevamente.\n")
        
        except ValueError:
            print("\nAlguna de las entradas ingresadas no es válida, intenta nuevamente.\n")
            
iniciar_programa()