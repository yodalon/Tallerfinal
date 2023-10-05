import math

# Valores de las coordenadas cilíndricas
x = 25.0
y = 30.0  
z = 3.0

# Calcula las coordenadas esféricas
rc= math.sqrt(x**2 + y**2)
theta = math.atan2(y,x)
theta_final = math.degrees(theta)
z=z
# Imprime las coordenadas esféricas
print(f"Coordenadas Esféricas:")
print(f"r_e = {rc}")
print(f"θ = {theta_final}")
print(f"φ = {y}")