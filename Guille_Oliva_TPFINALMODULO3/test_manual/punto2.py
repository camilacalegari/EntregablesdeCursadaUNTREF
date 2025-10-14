#DIPLO CALIDAD DE SOFTWARE
#TRABAJO PRACTICO INTEGRADOR FINAL MODULO 3
#ALUMNO/A: Guille Oliva

################################################

#PUNTO2

a = float(input("ingrese el valor de a: "))
b = float(input("ingrese el valor de b: "))
c = float(input("ingrese el valor de c: "))


discriminante = b*b - 4*a*c

if discriminante < 0:
    print("No tiene raíces reales")
else:
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print("Las raíces son:")
    print("x1 =", x1)
    print("x2 =", x2)
