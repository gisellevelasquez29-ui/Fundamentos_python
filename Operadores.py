#operadores aritmeticos
a = 10
b = 5

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
modulo = a % b
division_entera = a // b
potencia = a ** b


print(f"Suma: {suma}")

#CALCULADORA 

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
tipo_operacion = input("Ingrese la operación a realizar (suma, resta, multiplicacion, division, modulo, division_entera, potencia): ")

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
modulo = num1 % num2
division_entera = num1 // num2
potencia = num1 ** num2

if tipo_operacion == "suma":
    print(f"El resultado de la suma es: {suma}")
elif tipo_operacion == "resta":
    print(f"El resultado de la resta es: {resta}")
elif tipo_operacion == "multiplicacion":
    print(f"El resultado de la multiplicación es: {multiplicacion}")
elif tipo_operacion == "division":
    print(f"El resultado de la división es: {division}")
elif tipo_operacion == "modulo":
    print(f"El resultado del módulo es: {modulo}")
elif tipo_operacion == "division_entera":
    print(f"El resultado de la división entera es: {division_entera}")
elif tipo_operacion == "potencia":
    print(f"El resultado de la potencia es: {potencia}")


