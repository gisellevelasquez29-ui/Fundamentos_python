"""Crea actividad3_listas.py. Declara una lista canciones con 5 nombres de canciones
de tu género favorito."""

canciones = ["cancion1", "cancion2", "cancion3", "cancion4", "cancion5"]


"""2. Aplica los siguientes métodos en orden y muestra el estado de la lista después de
cada uno: append() para agregar una canción nueva al final; insert() para agregar
otra canción en la segunda posición; extend() para fusionar con esta lista: ["Bonus
Track 1", "Bonus Track 2"]."""

canciones.append("cancion6")
print(canciones)

canciones.insert(1, "cancion7")
print(canciones)

canciones.extend(["Bonus Track 1", "Bonus Track 2"])
print(canciones)

"""3. Usa remove() para eliminar una canción por su nombre y pop() para eliminar la
última canción, guardando el valor eliminado e imprimiéndolo."""
canciones.remove(canciones[3])
print(canciones)

cancion_eliminada = canciones.pop(6)
print(f"la cancion eliminada es: {cancion_eliminada}")


"""4. Usa sort() para ordenar la lista alfabéticamente y muéstrala ordenada."""
canciones.sort()
print(canciones)


"""5. Responde estas preguntas usando métodos: ¿Cuántas canciones tiene la playlist?
¿En qué posición está la primera canción que agregaste? ¿Cuántas veces aparece
el string 'Bonus Track 1'?"""

#la playlist tiene 7 canciones
#la primera cancion que agregue esta en la posicion 2
#Aparece dos veces en las diferentes listas

