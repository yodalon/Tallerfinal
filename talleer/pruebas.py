import math

class Conversion3D:
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    @staticmethod
    def grados_a_radianes(grados):
        return math.radians(grados)

    @staticmethod
    def radianes_a_grados(radianes):
        return math.degrees(radianes)

    def rectangular_a_cilindrico(self):
        rc = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        theta_final = self.radianes_a_grados(theta)
        return rc, theta_final, self.z

def main():
    while True:
        try:
            opcion = int(input("Seleccione el sistema original de sus coordenadas:\n1| Rectangular\n2| Cilíndrico\n3| Esférico\n4| Salir\n"))

            if opcion == 4:
                break

            if opcion == 1:
                num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                for i in range(num_tuplas):
                    x, y, z = input(f"Tupla {i+1}:\nIngrese x, y, z separados por espacios: ").split()
                    convertidor = Conversion3D(x, y, z)
                    resultado = convertidor.rectangular_a_cilindrico()
                    print("Coordenadas Cilíndricas:", resultado)

            # Aquí puedes agregar las otras conversiones (Cilíndrico a Rectangular, Rectangular a Esférico, etc.)

        except ValueError:
            print("Error: Ingreso de coordenadas no numéricas.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            break

if __name__ == "__main__":
    main()
