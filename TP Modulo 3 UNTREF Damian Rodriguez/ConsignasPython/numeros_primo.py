#Este codigo es de Damian Rodriguez
def es_primo(numero):
    
    if numero <= 1:
        return False
    
    
    if numero == 2:
        return True
    
    
    if numero % 2 == 0:
        return False
    
   
    i = 3
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 2
        
    return True

def main():
    try:
        # Vamos a ingresar un número
        numero = int(input("Ingrese un número para verificar si es primo: "))
        
        # aca vemos si es primo y mostramos el resultado
        if es_primo(numero):
            print(f"El número {numero} es primo.")
        else:
            print(f"El número {numero} no es primo.")
            
    except ValueError:
        print("Error: Tenes que ingresar un número entero que sea valido.")

if __name__ == "__main__":
    main()
