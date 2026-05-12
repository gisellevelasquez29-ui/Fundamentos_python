# listas

#estructura

#indice:   0           1           2
listas =["objeto_1", "objeto_2", "objeto_3"]
print(type(listas))

#lista mixta
lista_mixta = ["hola", 123, 3.14, True]
print(type(lista_mixta))


#lista de aprendices sena adso

#indice:        0          1         2         3        4
aprendices =["Giselle", "Felipe", "Sofia", "camilo", "luisa"]
print(aprendices)

#acceder a un elemento de la lista
print(aprendices[1])

#modificar un elemento de la lista
aprendices[2] = "maria"
print(aprendices)

#consultar rangos de elementos de la lista
print(aprendices[0:2])  # Muestra los elementos desde el índice 0 hasta el 1
print(aprendices[1::4]) 
print(aprendices[:3])


aprendices_ficha_3321349  = ["camilo", "andres", "maria", "pedro", "jorge"]
aprendices_ficha_1254785 = ["pedro","luisa", "sofia", "felipe", "ana", "carlos"]

#concatenar listas
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_1254785
print(aprendices_adso)

#unir listas con extend
aprendices_ficha_3321349.extend(aprendices_ficha_1254785)
print(aprendices_ficha_3321349)

#medir el largo con len
longitud_adso = len(aprendices_adso)
print(f"La longitud de la lista es: {longitud_adso}")

#contar elementos con count
count_felipe = aprendices_adso.count("felipe")
print(count_felipe)

#obtener el indice de un elemento con index
indice_felipe = aprendices_adso.index("felipe")
print(f"El índice de Felipe es: {indice_felipe}")

#copiar una lista con copy
nueva_lista_adso = aprendices_adso.copy()
print(nueva_lista_adso)

#agregar elementos (apppend e insert)
nueva_lista_adso.append("Fabian")
print(nueva_lista_adso)

nueva_lista_adso.insert(2, "Kevin")
print(nueva_lista_adso)

#eliminar elemento (remove y pop)
nueva_lista_adso.remove("pedro")
print(nueva_lista_adso)

nueva_lista_adso.pop(5)
print(nueva_lista_adso)

#comprobar si un elemento existe en la list (in)

if "maria" in nueva_lista_adso:
    print("maria esta en la lista")

#ordenar (sort y reverse)
nueva_lista_adso.sort()
print(nueva_lista_adso)

nueva_lista_adso.reverse()
print(nueva_lista_adso)







