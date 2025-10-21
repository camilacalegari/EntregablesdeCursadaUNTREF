""" 
Punto 1:
Escribir un programa que dado el ingreso de un número retorne si el mismo es
primo o no 
"""
def consultaprimo(numero):  
    if numero == 2:
        return True
    elif numero <= 1:
        return False
    elif numero % 2 == 0:
        return False
    valor = 3
    while valor * valor <= numero:
        if numero % valor == 0:
            return False
        valor += 2
    return True

def programa():
    
    while True:
        try:
            dato = input('Ingrese un número para saber si es primo.\n Ingrese "Salir" (S) para terminar el programa.')
            
            if (dato.lower() == 'salir' or dato.lower() =='s'):
                print("Chau!")
                break
            
            dato_int = int(dato)
            
            if consultaprimo(dato_int):
                print(f"El número {dato_int} es primo")
            else:
                print(f"El número {dato_int} no es un número primo.")
        
        except ValueError:
            print("\nLa entrada ingresada no es válida, intenta nuevamente.\n")

programa()
