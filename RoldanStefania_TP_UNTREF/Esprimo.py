# Pedimos al usuario que ingrese un número
numero = int(input("Ingresá un número: "))

# Suponemos que es primo hasta probar lo contrario
es_primo = True

# Los números menores o iguales a 1 no son primos
if numero <= 1:
    es_primo = False
else:
    # Probamos divisores desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

# Mostramos el resultado
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
