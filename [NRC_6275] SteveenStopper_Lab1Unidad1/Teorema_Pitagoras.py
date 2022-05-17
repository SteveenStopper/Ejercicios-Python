'''
Calcular el teorema de Pitágoras.
'''
CatA = float(input("Ingrese el cateto a: ")) #El usuario ingresara el valor del cateto a.
CatB = float(input("Ingrese el cateto b: ")) #El usuario ingresara el valor del cateto b.
Multilados = (CatA*CatA)+(CatB*CatB) #Tenemos una variavble la cual va a multiplicar (A*A)+(B*B).
Hipotenusa = Multilados**(1/2) #Ahora tenemos una variable llamada Hipotenusa la cual va a sacar la raiz de la formula anterior. 
print(Hipotenusa) #En esta se nos imprimira el resultado.