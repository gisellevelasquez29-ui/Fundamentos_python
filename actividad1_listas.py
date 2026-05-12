#ejercicio 1 Inventario de la Tienda Escolar


productos = ["lápiz", "cuaderno", "borrador", "regla", "colores", "pegamento"]
precios = [2000, 6000, 1000, 3000, 8000, 5000]
cantidades = [50, 30, 100, 20, 10, 15]
cantidad_producto = len(productos)

print("inventario de tienda escolar:"
      "\nProductos:", productos,
      "\nPrecios:", precios,
      "\nCantidades:", cantidades)

print(f"el producto: {productos[0]} tiene un precio de {precios[0]} y una cantidad de {cantidades[0]}")
print(f"el producto: {productos[1]} tiene un precio de {precios[1]} y una cantidad de {cantidades[1]}")
print(f"el producto: {productos[2]} tiene un precio de {precios[2]} y una cantidad de {cantidades[2]}")
print(f"el producto: {productos[3]} tiene un precio de {precios[3]} y una cantidad de {cantidades[3]}")
print(f"el producto: {productos[4]} tiene un precio de {precios[4]} y una cantidad de {cantidades[4]}")
print(f"el producto: {productos[5]} tiene un precio de {precios[5]} y una cantidad de {cantidades[5]}")

print(type(productos)) #es class list
print(type(productos[0])) # es class str



