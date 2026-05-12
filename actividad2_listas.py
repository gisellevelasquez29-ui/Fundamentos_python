"""1. Crea actividad2_listas.py con la siguiente lista de temperaturas registradas durante
dos semanas (14 días): temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18,
20, 22, 19]."""

#indice:        0   1   2   3   4   5   6   7   8   9   10  11  12  13
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19]


"""2. Usa indexación para imprimir la temperatura del primer día, el último día, el día 7
(mitad) y el penúltimo día, usando tanto índices positivos como negativos."""
print(f"Temperatura del primer dia:{temperaturas[0]}")
print(f"Temperatura del último dia:{temperaturas[-1]}")
print(f"Temperatura del día 7:{temperaturas[6]}")
print(f"Temperatura del penúltimo día:{temperaturas[-2]}")


"""3. Usa slicing para extraer e imprimir: la primera semana (días 1–7), la segunda
semana (días 8–14), solo los días pares de toda la quincena y la lista de
temperaturas en orden invertido."""

print(f"Temperaturas de la primera semana:{temperaturas[0:7]}")
print(f"Temperaturas de la segunda semana:{temperaturas[7:14]}")

print(f"Temperaturas de los días pares:{temperaturas[0:14:2]}")  
print(f"Temperaturas en orden invertido:{temperaturas[::-1]}") 


"""4. Calcula e imprime la temperatura promedio de cada semana por separado usando
sum() y len() aplicados a los slices.
5. Bonus: Determina cuál de las dos semanas tuvo mayor temperatura promedio y
muestra el resultado con un mensaje descriptivo."""

promedio_primera_semana = sum(temperaturas[0:7])/len(temperaturas[0:7])
promedio_segunda_semana = sum(temperaturas[7:14])/len(temperaturas[7:14])

print(f"Promedio de la primera semana: {promedio_primera_semana}")
print(f"Promedio de la segunda semana: {promedio_segunda_semana}")

if promedio_primera_semana > promedio_segunda_semana:
    print("La primera semana tuvo mayor temperatura promedio.")
else:
    print("La segunda semana tuvo mayor temperatura promedio.")