print("Hello World")


#comentario de una sola linea

nombre = "Giselle"
apellido = "Velasquez"
edad = 20
altura = 1.56
activo = True
correo = "giselle2005tt@gmail.com"
telefono = "3213355669"

#pasar el telefono a entero

telefono_int = int(telefono)

print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(telefono_int), telefono_int)


##casteo  convertir un tipo de dato a otro
edad_float = float(edad)
altura_int = int(altura)

print(type(edad_float), edad_float)
print(type(altura_int), altura_int)

"""
comentarios de varias lineas

"""

#Indentación o sangría

if 5 > 2:
    print ("5 es mayor que 2")
else:
    print ("5 es menor que 2")

#input

nombre_usuario = input("Ingrese su nombre: ")
print (nombre_usuario)

edad_usuario = int(input("Ingrese su edad: "))
print (edad_usuario)

print (f"Hola {nombre_usuario}, tu edad es {edad_usuario} años")


