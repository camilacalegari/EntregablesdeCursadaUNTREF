# Verificar si un número es primo

num = int(input("Ingresa un número: "))

if num <= 1:
    print(f"{num} no es un número primo.")
else:

    es_primo = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break

    if es_primo:
        print(f"{num} es un número primo.")
    else:
        print(f"{num} no es un número primo.")
