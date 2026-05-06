# actividad 3 

# 1. Solicitar datos
peso = float(input("Ingrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en metros: "))

# 5. Validación de datos si es valor negativo saldra mensje de error
if peso <= 0 or estatura <= 0:
    print("Error: El peso y la estatura deben ser valores positivos.")
else:
    # 2. Calcular Indise de Massa Corporal (IMC)
    imc = peso / (estatura ** 2)

    # 3. Clasificación segun el resultado del IMC
    if imc < 18.5:
        clasificacion = "Bajo peso"
    elif imc < 25:
        clasificacion = "Normal"
    elif imc < 30:
        clasificacion = "Sobrepeso"
    else:
        clasificacion = "Obesidad"

    # 4. Mostrar resultados
    print("\n--- Resultados ---")
    print(f"IMC: {round(imc, 2)}")
    print(f"Clasificación: {clasificacion}")

