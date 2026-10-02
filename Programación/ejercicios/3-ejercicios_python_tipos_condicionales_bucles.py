#Ejercicio 1. Control de notas
# Crea una lista llamada notas con al menos 10 calificaciones numéricas.
# El programa debe:
# Mostrar todas las notas.
# Calcular cuántas notas están aprobadas y cuántas suspendidas.
# Condición: Debe utilizar listas, bucle for, operadores de comparación y condicionales.
notas = [5,3,5,6,3,8,2,5,3,8]
aprobadas=0
desaprobados=0
for nota in notas:
    if nota >5:
        aprobadas=aprobadas+1
    else :
        desaprobados=desaprobados+1

print(notas)
print("Contar notas aprobados:", aprobadas)
print("Contar notas desaprobados", desaprobados)

suma_notas=0
contar_notas=0
# Calcular la nota media-----------------------------------------------------
for nota in notas:
    suma_notas =suma_notas + nota
    contar_notas=contar_notas+1

print("promedio:",suma_notas/contar_notas)
# Otra manera----------------------------------------------------------------
promedio=sum(notas)/len(notas)
print(promedio)

#Mostrar la nota más alta y la nota más baja.
for nota > notas:
    nota_alta=nota
print("nota alta:", nota_alta)


# Indicar si la media final está aprobada o suspendida.
if promedio > 5:
    print("La media está aprobada")
else:
    print("la media está suspendida")


#Ejercicio 2. Carrito de la compra
#Crea dos listas: una con nombres de productos y otra con sus precios.
productos = ["pan", "leche", "arroz", "huevos"]
precios = [1.20, 6, 2, 16]
# El programa debe:
# Mostrar el total final que debe pagarse.
# Condición: Debe utilizar zip, un acumulador, if y operadores aritméticos.
precio_total=0
# Mostrar cada producto con su precio.
for producto,precio in zip(productos,precios):
    print(producto,precio)
# Calcular el precio total de la compra.
for precio in precios:
    precio_total= precio_total + precio
print("precio total de la compra: ", precio_total)
# Aplicar un descuento del 10% si el total supera 20 euros.
if precio_total > 20:
    total_descuento=precio_total*0.9
else:
    total_descuento=precio_total
print("Total con descuento:",total_descuento)


