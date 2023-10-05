import math

class Conversion3D:
    def __init__(self, x, y, z, sistema_original="Rectangulares"):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.sistema_original = sistema_original

    @staticmethod
    def grados_a_radianes(grados):
        return grados * (math.pi / 180)

    @staticmethod
    def radianes_a_grados(radianes):
        return radianes * (180 / math.pi)

    

    def coordenadas_esfericas(self):
        if self.sistema_original == "Rectangulares":
            r_esfericas = math.sqrt(self.x**2 + self.y**2 + self.z**2)
            phi_esfericas = math.atan2(self.y, self.x)
            theta_esfericas = math.acos(self.z / r_esfericas)
            return r_esfericas, self.radianes_a_grados(phi_esfericas), self.radianes_a_grados(theta_esfericas)
        elif self.sistema_original == "Cilíndricas":
            rc = math.sqrt(self.x**2 + self.y**2)
            r_esfericas = math.sqrt(rc + self.z**2)
            phi_esfericas = self.grados_a_radianes(self.y)
            theta_esfericas = math.atan2(self.z,  r_esfericas)
            return r_esfericas, self.radianes_a_grados(phi_esfericas), self.radianes_a_grados(theta_esfericas)
        elif self.sistema_original == "Esféricas":
            return self.x, self.y, self.z
        else:
            raise ValueError("Sistema de coordenadas original no válido")

def main():
    try:
        num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
        for i in range(num_tuplas):
            x, y, z, sistema_original = input(f"Tupla {i+1}: Ingrese x, y, z, y sistema original separados por espacios: ").split()
            convertidor = Conversion3D(x, y, z, sistema_original)
            
            print("Coordenadas Rectangulares:", convertidor.coordenadas_rectangulares())
            print("Coordenadas Cilíndricas:", convertidor.coordenadas_cilindricas())
            print("Coordenadas Esféricas:", convertidor.coordenadas_esfericas())
            print()
    
    except ValueError as e:
        print("Error:", e)
    except ZeroDivisionError:
        print("Error: Division by zero")

if __name__ == "__main__":
    main()


