import math

# Valores de las coordenadas esféricas
r_esferico = 5.0
theta = math.radians(15)  # Convierte 15 grados a radianes
phi = math.radians(15)  # Convierte 15 grados a radianes

# Calcula las coordenadas cartesianas
x = r_esferico * math.sin(theta) * math.cos(phi)
y = r_esferico * math.sin(theta) * math.sin(phi)
z = r_esferico * math.cos(theta)

# Imprime las coordenadas cartesianas
print(f"Coordenadas Cartesianas:")
print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")
