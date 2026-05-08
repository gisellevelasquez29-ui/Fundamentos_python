#ejercicio 1

nombre = "felipe"
producto = 20000
promedio_asignaturas = 4.5
print(f"mi nombre es {nombre}, el precio del producto es {producto} y mi promedio de asignaturas es {promedio_asignaturas}")

#ejercicio 2

variable_1_entera = int(input("ingresa un numero entero: "))
variable_2_entera = int(input("ingresa otro numero entero: "))
variable_float = float(input("ingresa un numero decimal: "))
variable_1_string = input("ingresa una cadena de texto: ")
variable_2_string = input("ingresa otra cadena de texto: ")

suma_numeros = variable_1_entera + variable_2_entera + variable_float
print(f"la suma de los numeros es: {suma_numeros}")

#ejercicio 3

base = 5
exponente = 3

resultado = base ** exponente
print(f"el resultado de {base} elevado a la {exponente} es: {resultado}")


#ejercicio 4

numeros = input("ingresa un numero entero: ")

raiz_cuadrada = float(numeros) ** 0.5

print(f"la raiz cuadrada de {numeros} es: {raiz_cuadrada}")


#ejercicio 5

nombre_estudiante = input("ingresa el nombre del estudiante: ")
nota_1 = float(input("ingresa la nota de la asignatura 1: "))
nota_2 = float(input("ingresa la nota de la asignatura 2: "))
nota_3 = float(input("ingresa la nota de la asignatura 3: "))
nota_4 = float(input("ingresa la nota de la asignatura 4: "))
nota_5 = float(input("ingresa la nota de la asignatura 5: "))

promedio = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print(f"el promedio de {nombre_estudiante} es: {promedio}")
 

#ejercicio 6

numeroUno = 8 
numeroDos = 2

print (f"antes de la variable auxiliar: numeroUno = {numeroUno} y numeroDos = {numeroDos}")

#uso de variable auxiliar

temp = numeroUno
numeroUno = numeroDos
numeroDos = temp

print (f"despues de la variable auxiliar: numeroUno = {numeroUno} y numeroDos = {numeroDos}")

#ejercicio 7

estado = True

if estado ==  (5==2) or (2>1):
    print(f"la condicion es {estado}")

#ejercicio 8

# Crear variable llamada Resultado
resultado = (9 / 2) + 8 * 2 - 1 + (4 + 2) ** 2 % 5

# Mostrar resultado
print("El resultado de la operación es:", resultado)


#ejercicio 9

#cuadrado
ladoCuadrado = 8

areaCuadrado = ladoCuadrado * ladoCuadrado
perimetroCuadrado = 4 * ladoCuadrado

print (f"el perimetro del cuadrado es {perimetroCuadrado} y su area {areaCuadrado}")

#triangulo

baseTriangulo = 9
alturaTriangulo = 8
ladoUnoTriamgulo = 8
ladoDosTriangulo = 8

areaTriangulo = (baseTriangulo * alturaTriangulo)/2
perimetroTriangulo = ladoDosTriangulo + ladoUnoTriamgulo + baseTriangulo

print (f"el area de el triangulo es {areaTriangulo} y su perimetro {perimetroTriangulo}")

#rectangulo

baseRectangulo = 8 
alturaRectangulo = 6

areaRectangulo = baseRectangulo * alturaRectangulo
perimetroRectangulo = (2 * baseRectangulo) + (2 * alturaRectangulo)

print(f"el area del triangulo es {areaRectangulo} y su perimetro es {perimetroRectangulo}")
# ejercicio 10

edad_persona = int(input("ingrese su edad: "))

# Condicionales para determinar la categoría
if edad_persona >= 0 and edad_persona <= 5:
    print("Categoría: Infante")

elif edad_persona >= 6 and edad_persona <= 10:
    print("Categoría: Niño")

elif edad_persona >= 11 and edad_persona <= 15:
    print("Categoría: Pre adolescente")

elif edad_persona >= 16 and edad_persona <= 18:
    print("Categoría: Adolescente")

elif edad_persona >= 19 and edad_persona <= 25:
    print("Categoría: Pre adulto")

elif edad_persona >= 26 and edad_persona <= 40:
    print("Categoría: Adulto")

elif edad_persona >= 41 and edad_persona <= 55:
    print("Categoría: Pre anciano")

elif edad_persona >= 56:
    print("Categoría: Anciano")

else:
    print("Edad no válida")

