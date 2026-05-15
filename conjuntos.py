#Conjuntos (sets)

#estructura de un conjunto

conjunto = set()
print(type(conjunto))

#creacion

lenguajes = {"python", "java", "c++", "javascript"}
print(lenguajes) #si hay dos iguales no las duplica

#metodos de modificacion

frutas = {"manzana", "banana", "naranja"}
frutas.add("pera") #agregar
frutas.add("manxana") #no se agrega pq ya existe
frutas.remove("banana") #elimina
frutas.discard("uva") #elimina pero no da error si no eciste
elem = frutas.pop() #elimina cualquier elemento y lo guarda en una variable
print(elem)

#verificar pertenencia In

print("manzana" in frutas) #true
print("cobol" in lenguajes) #false


python_devs = {"Alice", "Bob", "Charlie", "David"}
java_devs = {"David", "Eve", "Frank", "Bob", "Grace"}

# Operaciones con conjuntos

# Unión
todos = python_devs | java_devs  # Todos los elementos
union = python_devs.union(java_devs)
print(todos)

# Diferencia
print(python_devs - java_devs)  # Elementos en python_devs pero no en java_devs