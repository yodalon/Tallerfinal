import math

class Conversion3D:
     
    def __init__(self,x, y, z):
        self.x = float (x)
        self.y = float (y)
        self.z = float (z)

    @staticmethod
    def redondear_decorador(func):
        def wrapper(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return tuple(round(x) if isinstance(x, (int, float)) else x for x in resultado)
        return wrapper

    @staticmethod
    def grados_a_radianes (grados):
        return math.radians(grados)
    @staticmethod
    def radianes_a_grados (radianes):
        return math.degrees(radianes)
   
    @redondear_decorador
    def rectangular_a_cilindrico(self):
        rc = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        theta_final = self.radianes_a_grados(theta)
        return rc, theta_final, self.z
    
    @redondear_decorador
    def rectangular_a_esferico(self):
        r_esferico = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        phi = math.atan2(self.y,self.x)
        phi_final = self.radianes_a_grados(phi)
        theta = math.acos(r_esferico,self.z)
        thetafinal =self.radianes_a_grados(theta)
        return r_esferico, phi_final, thetafinal
    
    @redondear_decorador
    def cilindrico_a_rectangular(self):
        rc = math.sqrt (self.x**2 + self.y**2)
        x_rectagular = rc * math.cos(self.y)
        y_rectagular = rc * math.sin(self.y)
        z_rectangular = self.z
        return x_rectagular, y_rectagular, z_rectangular
    
    @redondear_decorador
    def cilindrico_a_esferico(self):
        rc= math.sqrt(self.x**2 + self.y**2)
        r_esferico = math.sqrt((rc) + self.z**2)
        theta = math.atan2(rc,self.z)
        theta_final = math.degrees(theta)
        return r_esferico, theta_final, self.y
    @redondear_decorador
    def esferico_a_rectangular(self):
        x = self.x * math.sin(self.y) * math.cos(self.y)
        y = self.x * math.sin(self.y) * math.sin(self.y)
        z = self.x * math.cos(self.y)
        return x, y, z
    
    @redondear_decorador
    def esferico_a_cilindrico(self):
        rc= self.x * math.sin(self.z)
        y=self.y
        re=math.sqrt(self.x**2 + self.y**2 + self.z**2)
        z= re * math.cos(self.y)
        return rc, y, z
def main():
    while True:
        try:
            opcion = int(input("Seleccione el sistema original de sus coordenadas: \n  \t 1| Rectangular \n \t 2| Cilíndrico \n  \t 3| Esferico \n \t 4| Salir \n \t"))
            if opcion == 1:
                while True:
                    opcion = int(input("Seleccione el sistema al que desea convertir: \n \t 1| Cilíndrico \n \t 2| Esferico \n \t 3| Salir \n \t"))
                    if opcion == 1: 
                        num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                        for i in range(num_tuplas):
                            x, y, z = input(f"Tupla {i+1}: \n Ingrese x, y, z : ").split()
                            convertidor = Conversion3D(x, y, z)
                            resultado = convertidor.rectangular_a_cilindrico()
                            print("Coordenadas Cilíndricas:", resultado)

                    elif opcion == 2:
                            num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                            for i in range(num_tuplas):
                                x, y, z = input(f"Tupla {i+1}: \n Ingrese x, y, z : ").split()
                                convertidor = Conversion3D(x, y, z)
                                resultado = convertidor.rectangular_a_esferico()
                                print("Coordenadas Esféricas:", resultado)
                    elif opcion == 3:
                        print("Saliendo del programa")
                        break
            elif opcion ==2:
                while True:
                    opcion = int(input("Seleccione el sistema al que desea compartir: \n \t 1| Rectangular \n \t 2| Esférico \n \t 3| salir \n \t"))
                    if opcion == 1: 
                            num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                            for i in range(num_tuplas):
                                x, y, z = input(f"Tupla {i+1}: \n  Ingrese r=x, φ=y, θ=z : ").split()
                                convertidor = Conversion3D(x, y, z)
                                resultado = convertidor.cilindrico_a_rectangular()
                                print("Coordenadas Rectangulares:", resultado)
                    elif opcion ==2:
                            num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                            for i in range(num_tuplas):
                                x, y, z = input(f"Tupla {i+1}: \n  Ingrese r=x, φ=y, θ=z : ").split()
                                convertidor = Conversion3D(x, y, z)
                                resultado = convertidor.cilindrico_a_esferico()
                                print("Coordenadas Esféricas:", resultado)
                    elif opcion == 3:
                        print("Saliendo del programa")
                        break
            elif opcion == 3:
                while True:
                    opcion = int(input("Seleccione el sistema al que desea compartir: \n \t 1| Rectangular \n \t 2|Cilíndrico \n \t 3| salir \n \t"))
                    if opcion == 1:
                            num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                            for i in range(num_tuplas):
                                x, y, z = input(f"Tupla {i+1}: \n  Ingrese r=x, φ=y, θ=z : ").split()
                                convertidor = Conversion3D(x, y, z)
                                resultado = convertidor.esferico_a_rectangular()
                                print("Coordenadas Esféricas:", resultado)
                    elif opcion == 2: 
                            num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                            for i in range(num_tuplas):
                                x, y, z = input(f"Tupla {i+1}: \n  Ingrese r=x, φ=y, θ=z : ").split()
                                convertidor = Conversion3D(x, y, z)
                                resultado = convertidor.esferico_a_cilindrico()
                                print("Coordenadas Esféricas:", resultado)
                    elif opcion == 3:
                        print("Saliendo del programa")
                        break
            elif opcion == 4:
                 print("Saliendo del programa")
                 break
        except ValueError:
            print("Error: Ingreso de coordenadas no numéricas.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
                    
if __name__ == "__main__":
    main()
                
