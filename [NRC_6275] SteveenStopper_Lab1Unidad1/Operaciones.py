'''
Ingresar dos números y realizar todas las operaciones aritméticas.
'''

numero1 = float(input("Ingrese el primer numero: ")) #El usuario ingresa el primer valor
numero2 = float(input("Ingrese el segundo numero: ")) #El usuario ingresa el segundo valor
suma = numero1 + numero2 #Variable con formula de suma.
resta = numero1 - numero2 #Variable con formula de resta.
multiplicacion = numero1 * numero2 #Variable con formula de multiplicacion.

if (numero2 == 0): #En caso de que el valor sea igual a cero este no se podra dividir.
    print("La suma es: ", suma, "\n La resta es: ", resta, "\n La multiplicacion es: ",
    multiplicacion, "\n Division: No es posible dividir para cero." )
else: #Si el valor no es igual a cero este podra dividirse.
    Division = numero1 / numero2
    print("La suma es: ", suma, "\n La resta es: ", resta, "\n La multiplicacion es: ",
    multiplicacion, "\n La division es: ", Division )