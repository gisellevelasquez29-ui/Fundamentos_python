#operadores logicos
 

#and
print(True and True) #si ambas son verdaderas devuelve true
print(False and False) #si ambas son falsas devuelve false
print(True and False) #si una de las dos es falsa devuelve false
print(False and True)

#or

print(True or True) #si ambos son verdaderos devuelve true
print(False or False)#si ambos son falsos devueve truw
print(True or False) #si una de las dos es verdadera devuelve true
print(False or True)#si una de las dos es verdadera devuelve true

#not

print(not True) #si es verdadero devuelve falso
print(not False) #si es falso devuelve verdadero



print(5>3 and 2<4) #true
print(5>3 and 2>4) #false
print(2>3 and 2<4) #false
print(2>3 and 5<4) #false

print(5>3 or 2<4) #true
print(5>3 or 2>4) #true
print(2>3 or 2<4) #true
print(2>3 or 5<4) #true

print(not 5>3) #false
print(not 2>3) #true
