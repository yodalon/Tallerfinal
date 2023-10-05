import math

# Valores de las coordenadas cilíndricas
x = 25.0
y = 30.0  
z = 3.0

# Calcula las coordenadas esféricas
r_esferico = math.sqrt(x**2 + y**2 + z**2)
phi = math.atan2(y,x)
phi_final = math.degrees(phi)
theta = math.acos(r_esferico,z)
thetafinal = math.degrees(theta)
# Imprime las coordenadas esféricas
print(f"Coordenadas Esféricas:")
print(f"r_e = {r_esferico}")
print(f"θ = {phi_final}")
print(f"φ = {y}")