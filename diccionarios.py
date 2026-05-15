#diccionarios

#creacion de un diccionario

#estructura

diccionario = {
    "clave_1": "valor_1",
    "clave_2": "valor_2",
    "clave_3": "valor_3"
}

#diccionario vacio

diccionario_vacio = {}

#diccionsario con elementos

diccionario_aprendiz= {
    "nombre": "Juan",
    "apellido": "Perez",
    "programa" : "ADSO",
    "ficha": "12345",
    "edad": 25,
}

print(type(diccionario_aprendiz)) #class dict

#obtener un valor del diccionario
print(diccionario_aprendiz["nombre"]) #Juan
print(diccionario_aprendiz.get("apellido"))

#obtener dolo las claves del diccionario
print(diccionario_aprendiz.keys())

#obtener solo os valores del diccionario
print(diccionario_aprendiz.values())

#obtener las claves y los valores del diccionario
print(diccionario_aprendiz.items())

#agregar un nuevo elemento al diccionario
diccionario_aprendiz["correo"] = "juan.perez@example.com"
#modificar valor de una clave existente
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz)

#metodo update para actualaiza o modifica y si no esta creado lo agrega

diccionario_aprendiz.update({"nombre": "Liliana"})
diccionario_aprendiz.update({"ciudad" :  "Duitama"})
print(diccionario_aprendiz)

#comprobar pertenencia (in) comprobar si esta booleano

if "ficha" in diccionario_aprendiz:
    print("La clave 'ficha' existe en el diccionario")


#recorrer un diccionario con un ciclo for

for clave in diccionario_aprendiz.keys():
    print(clave)

#recorrer solo los valores de un diccionario

for valor in diccionario_aprendiz.values():
    print(valor)

#recorrer los items son para recorrer las claves y el valor

for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}: {valor}")

#eliminar un elemntos del diccionario pop

diccionario_aprendiz.pop()#ultimo
print(diccionario_aprendiz)

diccionario_aprendiz.pop("ciudad")
print(diccionario_aprendiz)

diccionario_aprendiz.clear() #eliminar todo el diccionario
print(diccionario_aprendiz)



#DICCIONARIOS ANIDADOS  

aprendices = {
    "aprendiz_1": {
        "nombre": "Jairo",
        "apellido": "Perez",
        "programa" : "ADSO",
        "ficha": "12345",
        "edad": 25,
    },
    "aprendiz_2": {
        "nombre": "Pedro",
        "apellido": "Gomez",
        "programa" : "SST",
        "ficha": "67890",
        "edad": 30,
    },
    "aprendiz_3" : {
        "nombre": "Maria",
        "apellido": "Lopez",
        "programa" : "ADSO",
        "ficha": "54321",
        "edad": 28,
    }
}

#acceder a un valor en un diccionario aninado
print(aprendices["aprendiz_1"]["nombre"])

#recorrer un diccionario aninado

for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    for clave, valor in datos.items():
        print(f"{clave}:{valor}")


