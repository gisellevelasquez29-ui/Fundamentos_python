# actividad de calculadora de notas

#ingresar notas
print("=" * 45)
print("calculadora de notas")
print("=" * 45)
nota_1 = float(input("ingresa tu primera nota:"))
nota_2 = float(input("ingresa tu segunda nota:"))
nota_3 = float(input("ingresa tu tercer nnota:")) 

# calcular promedio
promedio = (nota_1 + nota_2 + nota_3) / 3
promedio_redondeado = round(promedio, 2)
# nota maxima
NOTA_MAXIMA = 5.0

# calcular puntos faltantes para aprobar
puntos_faltantes = round(max(0, NOTA_MAXIMA - promedio), 2)


# determinar si se alcanza la nota minima para aprobar
nota_minima = 3.0
aprueba = promedio >= nota_minima

# deeterminar si aprueva o no 

print ("\n========RESULTADO============")

print (f"promedio: {promedio_redondeado}")
print (f"faltante: {puntos_faltantes}")

if nota_minima:
    print ("Estado: Aprueba✅")
else:
    print ("Estado: No Aprueba❌")

