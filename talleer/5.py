"""EJERCICIO CON WHILE 
Hacer una calculadora en phyton usando el ciclo while teniendo en cuneta lo siguiente: 
El usuario debe ingresar los datos a tener en cuenta en las operaciones
la calculadora debe tener las siguientes operaciones
    Suma
    Resta
    Multiplicacion
    Division: para realizar esta operacion debe tener una restriccion que evite que el usuario ingrese 0 como divisor
    Factorial de un numero ingresado
    Raiz cuadrada, debe especificar que el dato a ingresar debe ser positivo
    Cambiar numeros
    Salir
    Crear un codigo que arroje el resultado de la operacion escogida por el usuario
"""

import math
while True:   
    opcion = int(input("Selecciona una figura \n \t 1. Suma \n \t 2. Resta \n \t 3. Multiplicación \n \t 4. Division\n \t 5. Factorial \n \t 6. Raiz Cuadrada \n \t 7. Cambiar numeros \n \t 8. Salir \n"))
    
    if opcion == 1:
        dato1 = int (input("Ingrese un numero (dato 1): "))
        dato2 = int (input("Ingrese otro numero (dato 2): "))
        resultado = (dato1 + dato2)
        print (f"La suma de los datos es: {resultado}")
        
    elif opcion == 2: 
        dato1 = int (input("Ingrese un numero (dato 1): "))
        dato2 = int (input("Ingrese otro numero (dato 2): "))
        resultado = (dato1 - dato2)
        print (f"La suma de los datos es: {resultado}")
        
    elif opcion == 3:
        dato1 = int (input("Ingrese un numero (dato 1): "))
        dato2 = int (input("Ingrese otro numero (dato 2): "))
        resultado = (dato1 * dato2)
        print (f"La suma de los datos es: {resultado}")
        
    elif opcion == 4:
        dato1 = int (input("Ingrese un numero (dato 1): "))
        dato2 = int (input("Ingrese otro numero (dato 2): "))
        if dato2 == 0:
            print("Error: El divisor no puede ser 0.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    
    elif opcion == 5:
        num = int(input("Ingresa un número entero positivo: "))
        if num < 0:
            print("Error: Ingresa un número positivo.")
        else:
            factorial = 1
            for i in range(1, num + 1):
                factorial *= i
            print(f"El factorial de {num} es: {factorial}")
            
    elif opcion == 6:
        num = float(input("Ingresa un número positivo: "))
        if num < 0:
            print("Error: Ingresa un número positivo.")
        else:
            raiz_cuadrada = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es: {raiz_cuadrada}")
            
    elif opcion == 7:
        num1 = float(input("Ingresa el nuevo primer número: "))
        num2 = float(input("Ingresa el nuevo segundo número: "))
    elif opcion == 8:
        print("Saliendo del programa.")
        break
    