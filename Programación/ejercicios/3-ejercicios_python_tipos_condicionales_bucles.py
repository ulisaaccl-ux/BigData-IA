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
nota_mas_alta= notas[0]
nota_mas_baja= notas[0]
for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta=nota
    if nota < nota_mas_baja:
        nota_mas_baja=nota
print("nota alta:", nota_mas_alta)
print("nota baja:", nota_mas_baja)


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

#Ejercicio 3. Registro de Alumno
#Crea un diccionario llamado alumno con los siguientes datos:
#El programa debe:
#Mostrar todos los datos del alumno.

#Condición: Debe utilizar diccionarios, if, elif, else y operadores lógicos.

alumno = {"nombre": "Cesar", "Edad": 24 ,"curso": "Python", "nota_media":7 , "faltas":4}
print ("datos del alumno:",alumno)

#Indicar si el alumno aprueba. Aprueba si su nota_media es mayor o igual que 5.
if alumno["nota_media"] >=5:
    print(" Aprueba")
#Indicar si debe recibir un aviso. Recibe aviso si tiene más de 10 faltas.
if alumno ["faltas"] >10:
    print ("Debe recibir un aviso")

#Mostrar un mensaje final combinando el resultado académico y el aviso por faltas.

if alumno["nota_media"] >=5 and alumno ["faltas"] >10:
    print("Aprueba pero debe recibir un aviso")
elif alumno["nota_media"] >=5 and alumno ["faltas"] <=10:
    print("Aprueba y no debe recibir un aviso")
elif alumno["nota_media"] <5 and alumno ["faltas"] >10:
    print("No aprueba y debe recibir un aviso")
else:
    print("No aprueba y no debe recibir un aviso")

#Ejercicio 4. Números pares, impares y múltiplos
#Usando range, recorre los números del 1 al 50.
#El programa debe:
#Contar cuántos números son pares.
#Contar cuántos números son impares.
#Contar cuántos números son múltiplos de 5.
#Mostrar los tres resultados finales.
#Condición: Debe utilizar for, range, el operador módulo % y contadores.
contar_pares=0
contar_impares=0
contar_multiplos_5=0
for i in range (1,51):
    if i%2==0:
        contar_pares=contar_pares+1
    else:
        contar_impares=contar_impares+1

    if i%5==0:
        contar_multiplos_5=contar_multiplos_5+1

print("Números pares:", contar_pares)
print("Números impares:", contar_impares)
print("Números múltiplos de 5:", contar_multiplos_5)


#Ejercicio 5. Validación de contraseña
#Crea una variable llamada password con una contraseña de prueba.
#El programa debe:
# Comprobar si la contraseña tiene al menos 8 caracteres.
# Comprobar si contiene el símbolo @.
# Comprobar que no sea igual a 12345678.
# Si cumple todas las condiciones, mostrar Contraseña válida.
# En caso contrario, mostrar Contraseña no válida.
#Condición: Debe utilizar strings, len, operadores lógicos y condicionales. Para comprobar si aparece @ dentro
#del texto puede utilizarse "@" in password.
