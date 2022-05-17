'''
Volumen de la esfera.
'''
from cmath import pi #Libreria de pi.

radio = float(input("Ingrese el radio de la esfera: ")) #El usuario ingresara el valor del radio.
volumen = 4/3 * pi * radio ** 3 # Variable con la formula de la esfera.

print('El volumen de la esfera es {} unidad cubicas'.format(volumen)) #Se imprime el resultado del usuario.