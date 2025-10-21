#DIPLO CALIDAD DE SOFTWARE
#TRABAJO PRACTICO INTEGRADOR FINAL MODULO 3
#ALUMNO/A: Guille Oliva

################################################

#PUNTO1

while True:
    numero_elegido = int(input("ingrese el número (0 para salir): "))

    if numero_elegido == 0:
        print("se finaliza el programa")
        break

    divisores = 0

    for i in range(1, numero_elegido + 1):
        if numero_elegido % i == 0:
            divisores = divisores + 1

    if divisores == 2:
        print("El numero es primo")
    else:
        print("El numero no es primo")