#operadores aritmeticos
a = 10
b = 5

#suma
suma = a + b
print(f"la Suma de {a} y {b} es: {suma}")

#resta
resta = a - b
print(f"la Resta de {a} y {b} es: {resta}")

#multiplicacion
multiplicacion = a * b
print(f"la Multiplicación de {a} y {b} es: {multiplicacion}")

#division flotante
division = a / b
print(f"la División de {a} y {b} es: {division}")

#division entera
division_entera = a // b
print(f"la División Entera de {a} y {b} es: {division_entera}")

#modulo o residuo
modulo = a % b
print(f"el Módulo de {a} y {b} es: {modulo}")

#potencia o exponente
potencia = a ** b
print(f"la Potencia de {a} y {b} es: {potencia}")


#precedencia de operadores
resultado = a + b * 2
print(f"El resultado de la operación {a} + {b} * 2 es: {resultado}")

resultado_2 = (a + b) * 2
print(f"El resultado de la operación ({a} + {b}) * 2 con paréntesis es: {resultado_2}")

resultado_3 = a + b //3
print(f"El resultado de la operación {a} + {b} // 3 es: {resultado_3}")

resultado_4 = (a + b) // 3
print(f"El resultado de la operación ({a} + {b}) // 3 es: {resultado_4}")

resultado_5 = a * (b // 3)
print(f"El resultado de la operación {a} * ({b} // 3) es: {resultado_5}")

ejercicio = a + b * 2 - (a // b) ** 2
# 10 + 5 * 2 - (10 // 5) ** 2
# 10 + 10 - (2) ** 2
# 10 + 10 - 4
# 20 - 4
# 16
print(f"El resultado de la operación {a} + {b} * 2 - ({a} // {b}) ** 2 es: {ejercicio}")

#libreriaas matematicas
import math

print(math.pi)
print(math.e)
print(math.sqrt(16))


import random

random.random() # numero aleatorio entre 0 y 1
numero_aleatorio = random.randint(1, 10) 
print(numero_aleatorio)



























