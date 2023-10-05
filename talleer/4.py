import math

 

class Conversion3D:
    def __init__(self, tipo_sistema, x, y, z):
        self.tipo_sistema = tipo_sistema
        self.x = x
        self.y = y
        self.z = z

 

    def coordenadas_cartesianas(self):
        if self.tipo_sistema == "c":
            return (self.x, self.y, self.z)
        elif self.tipo_sistema == "e":
            r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            theta = math.atan2(self.y, self.x)
            phi = math.acos(self.z / r)
            return (r, theta, phi)
        elif self.tipo_sistema == "c":
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.atan2(self.y, self.x)
            return (r, theta, self.z)
        else:
            return None

 

    def coordenadas_cilindricas(self):
        if self.tipo_sistema == "c":
            return (self.x, self.y, self.z)
        elif self.tipo_sistema == "e":
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.atan2(self.y, self.x)
            return (r, theta, self.z)
        elif self.tipo_sistema == "c":
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.atan2(self.y, self.x)
            return (r, theta, self.z)
        else:
            return None

 

    def coordenadas_esfericas(self):
        if self.tipo_sistema == "c":
            r = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
            theta = math.atan2(self.y, self.x)
            phi = math.acos(self.z / r)
            return (r, theta, phi)
        elif self.tipo_sistema == "e":
            return (self.x, self.y, self.z)
        elif self.tipo_sistema == "c":
            r = math.sqrt(self.x ** 2 + self.y ** 2)
            theta = math.atan2(self.y, self.x)
            return (r, theta, self.z)
        else:
            return None

 

# Ejemplo de uso:
# Coordenadas iniciales en el sistema esférico
conversion = Conversion3D("e", 2.0, math.pi/4, math.pi/3)

 

# Conversión a coordenadas cartesianas
cartesianas = conversion.coordenadas_cartesianas()
print("Coordenadas cartesianas:", cartesianas)

 

# Conversión a coordenadas cilíndricas
cilindricas = conversion.coordenadas_cilindricas()
print("Coordenadas cilíndricas:", cilindricas)

 

# Conversión a coordenadas esféricas
esfericas = conversion.coordenadas_esfericas()
print("Coordenadas esféricas:", esfericas)

   
