import math

x = float(input("Ingrese el valor de X: "))
y = float(input("Ingrese el valor de Y: "))
z = float(input("Ingrese el valor de Z: "))

#calculo
rc = math.sqrt (x**2 + y**2)
x_rectagular = rc * math.cos(y)
y_rectagular = rc * math.sin(y)
z_rectangular = z

print(f"Coordenadas Cartesianas:")
print(f"x = {x_rectagular}")
print(f"y = {y_rectagular}")
print(f"z = {z_rectangular}")