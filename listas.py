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
aprendices_ficha_1254785 = ["luisa", "sofia", "felipe", "ana", "carlos"]

#concatenar listas
aprendices_adso = aprendices_ficha_3321349 + aprendices_ficha_1254785
print(aprendices_adso)






