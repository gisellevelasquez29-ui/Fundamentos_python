# importar libreria para generar numero aleatorio
import random

print("🃏 Juego: 3 jugadores vs computadora")


#definir las cartas y sus valores
cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

valores = {
"A": 14, "K": 13, "Q": 12, "J": 11,
"10": 10, "9": 9, "8": 8, "7": 7,
"6": 6, "5": 5, "4": 4, "3": 3, "2": 2
}

#mostrar que cartas hay para elegir
print("Cartas disponibles:", cartas)


#ingresar nombres de los jugadores 
# Nombres
n1 = input("Nombre del Jugador 1: ")
n2 = input("Nombre del Jugador 2: ")
n3 = input("Nombre del Jugador 3: ")
#ingresar la carta escogida por cada jugador
# Elecciones
j1 = input(n1 + ", elige carta: ")
j2 = input(n2 + ", elige carta: ")
j3 = input(n3 + ", elige carta: ")


# Validación
# Validar que las cartas elegidas estén en la lista de cartas disponibles
carta_pc = random.choice(cartas)
if j1 in cartas and j2 in cartas and j3 in cartas:
    print("\n📋 Elecciones:")
print(n1, "eligió:", j1)
print(n2, "eligió:", j2)
print(n3, "eligió:", j3)

#mostrar la carta de la computadora
print("\n💻 Carta de la computadora:", carta_pc)

#convierte la carta de la computadora y las cartas de los jugadores a sus valores numericos para calcular las distancias
v_pc = valores[carta_pc]
v1 = valores[j1]
v2 = valores[j2]
v3 = valores[j3]

# veriuficar si algun jugador acerto la carta exacta de la computadora
if j1 == carta_pc:
    print("🏆 Gana", n1, "(acertó la carta exacta)")
elif j2 == carta_pc:
    print("🏆 Gana", n2, "(acertó la carta exacta)")
elif j3 == carta_pc:
    print("🏆 Gana", n3, "(acertó la carta exacta)")
else:


#distancias


    input("\n🔍 dale enter para revelar las distancias:")

#calcular la distancia entre las cartas de los jugadores y la carta de la computadora
d1 = abs(v1 - v_pc)
d2 = abs(v2 - v_pc)
d3 = abs(v3 - v_pc)

#muestra las distancias de cada jugador a la carta de la computadora
print("\n📊 Distancias:")
print(n1 + ":", d1)
print(n2 + ":", d2)
print(n3 + ":", d3)

#encuentra el minumo de las distancias para determinar el ganador
menor = min(d1, d2, d3)

#ganador

input("\n🏆 dale enter para revelar el ganador:")


#determina el ganador comparando las distancias de cada jugador a la carta de la computadora
if d1 == menor:
    print("🏆 Gana", n1, "(más cercano)")
elif d2 == menor:
    print("🏆 Gana", n2, "(más cercano)")
else:
    print("🏆 Gana", n3, "(más cercano)")
