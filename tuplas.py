#TUPLAS

#estructura de una tupla

#indice:     0                   1         2


tupla = ("elemento_1,", "elemento_2", "elemento_3")
print(type(tupla))

tupla_2 = "a", "b", "c"
print(type(tupla_2))

tupla_3 = ("hola",)
print(type(tupla_3))

tupla_4 = tuple("hola")
print(tupla_4)

tupla_mixta = ("hola", 123, 3.14, True, [1, 2, 3])
print(tupla_mixta)

#tupla de aprendices sena adso
aprendices =("Giselle", "Felipe", "Sofia", "camilo", "luisa")
print(aprendices)

#acceder a un elemento de la tupla
print(aprendices[2])

#modificar un elemento de la tupla
#aprendices[2] = "Paula" genera error pq las tuplas no son mutables

#cunsultar rangos de elementos de la lista
print(aprendices[0:2])
print(aprendices[1:4])
print(aprendices[1:])

#sumar dos tuplas
tupla_1 = (1, 2, 3)
tupla_2 = (4, 5, 6)
tupla_suma = tupla + tupla_2
print(tupla_suma)

#multiplicar una tupla
tupla_multiplicada = tupla_1 * 3
print(tupla_multiplicada)

# metodos de las tuplas

#meditr el largo con len()
print(len(aprendices))

#contar los elementos de una tupla con count()
print(aprendices.count("camilo"))

#obtener el indice de una tupla con index
print(aprendices.index("luisa"))

#modificar una tupla a lista(casteo)

print(type(aprendices)) #tupla
aprendices_lista = list(aprendices)
aprendices_lista.append("Paula")
print(type(aprendices_lista))

#lista a tupla

aprendices = tuple(aprendices_lista)
print(type(aprendices_lista))
print(aprendices)

#comrpobar pertenencia (in)

print("Giselle" in aprendices)
print("Leidy" in aprendices)

#empaquetar tuplas
programa_1 = "ADSO"
programa_2 = "SST"
programa_3 = "topografia"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)

#desempaquetar tuplas

tupla_desempaquetada = ("ADSO", "SST", "Topografia")
programa1, programa2, programa3 = tupla_desempaquetada
print(programa1)

#desempaquetar #2

tupla_ciudades = ("Bogota", "medellin", "cali")
ciudad_1, ciudad_2, ciudad_3 = tupla_ciudades
print(ciudad_1)
#iterar sobre una tupla con un cliclo for
for ciudad in tupla_ciudades:
    print(ciudad)
















