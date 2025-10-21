# Este código fue hecho por Matias Nazadek.

# Programa que dado el ingreso de un número retorna si el mismo es primo o no.
# Con try/except valido que el número ingresado sea entero positivo.

try:
    n = int(input("Ingresá un número: "))

    if n <= 0:
        print("Debe ser un número entero positivo.")
    elif n < 2:
        print("No es primo.")
    else:
        es_primo = True

        for i in range(2, n):
            if n % i == 0:
                es_primo = False
                break

        if es_primo:
            print("Es primo.")
        else:
            print("No es primo.")

except ValueError:
    print("Debe ser un número entero positivo.")