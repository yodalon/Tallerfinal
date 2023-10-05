import math

# Valores de las coordenadas cilíndricas
x = 5.0
y = 45.0  
z = 10.0

# Calcula las coordenadas esféricas
rc= math.sqrt(x**2 + y**2)
r_esferico = math.sqrt((rc)+ z**2)
theta = math.atan2(rc,z)
theta_final = math.degrees(theta)
z= math.atan2(rc,z)
# Imprime las coordenadas esféricas
print(f"Coordenadas Esféricas:")
print(f"r_e = {r_esferico}")
print(f"θ = {theta_final}")
print(f"φ = {y}")
