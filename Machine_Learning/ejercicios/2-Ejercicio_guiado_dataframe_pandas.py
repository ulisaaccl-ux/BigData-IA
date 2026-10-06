
# Ejercicio extra: Diccionario:

import pandas as pd
estudiantes = {
    "Ana": (23, 43, True),
    "Paco": (21, 38, False),
    "Marta": (19, 41, True),
    "Luis": (25, 35, False),
    "Elena": (22, 39, True),
    "Carlos": (20, 36, True),
    "Sara": (18, 34, False),
    "Miguel": (27, 45, False),
    "Lucia": (21, 42, True),
    "Andres": (24, 37, False)
}
df=pd.DataFrame(estudiantes, index=["Edad","Puntos","Estudios Superiores"])
print(df)

#Ejercicio extra : Lista de dicccionarios:


#Ejercicio 1. Crear la estructura de datos
#Crea una estructura de datos en Python que guarde toda la información de la tabla anterior.
#Piensa primero cuál es la forma más cómoda de organizar los datos: una lista para cada columna, un
#diccionario de listas o una lista de diccionarios.
#Recomendación: usa un diccionario donde cada clave sea una columna.
datos = {
    "nombre": [
        "Ana",
        "Paco",
        "Marta",
        "Luis",
        "Elena",
        "Carlos",
        "Sara",
        "Miguel",
        "Lucia",
        "Andres"],
    "edad": [23, 21, 19, 25, 22, 20, 18, 27, 21, 24],
    "puntos": [43, 38, 41, 35, 39, 36, 34, 45, 42, 37],
    "estudios_superiores": [
        True,
        False,
        True,
        False,
        True,
        True,
        False,
        False,
        True,
        False,]}
print("Ejercicio 1")
print(datos)

#Ejercicio 2. Crear un DataFrame
#Importa la librería pandas con el pseudónimo pd.
#Convierte la estructura de datos anterior en un DataFrame.
#Muestra la tabla completa por pantalla.

import pandas as pd
df=pd.DataFrame(datos)
print("Ejercicio 2")
print (df)

#Ejercicio 3. Explorar el DataFrame
#Usa métodos básicos de pandas para conocer mejor los datos antes de modificarlos.
#Debes mostrar las primeras filas, el tamaño del DataFrame, las columnas, los tipos de datos, la
#información general y las estadísticas básicas.
# 1. Primeras filas (Head)
print("Ejercicio 3")
print("--- Primeras filas ---") # Por defecto muestra 5 filas
print(df.head())
print("---Tamaño del DataFrame ---") #Filas y columnas
print(df.shape)
print("--- Columnas ---")#Nombre  de las columnas
print(df.columns)
print("--- Tipos de datos ---")#Tipos de datos de cada columna
print(df.dtypes)
print("--- Información general (info) ---")#Información general del DataFrame
df.info()
print("--- Estadísticas básicas  ---")# Estadistica de las columnas numéricas
print(df.describe())

#Ejercicio 4. Crear una regla de selección
#Queremos decidir si una persona es apta para el trabajo.
#Antes de programarlo, escribe la lógica con tus propias palabras.
#- Si tiene 22 años o más, será apta si tiene al menos 40 puntos.
#- Si tiene menos de 22 años, solo será apta si tiene estudios superiores y al menos 35 puntos.
#  En cualquier otro caso, no será apta.

print("Ejercicio 4")

#Logica :
# Si edad >=222 y puntos >=40 es apto
# edad < 22 y estudios superiores = True y puntos >=35 es apto 
#Caso ontrario no apto.

#Ejercicio 5. Añadir una nueva columna
#Añade al DataFrame una nueva columna llamada apto.
#La columna debe contener True si la persona es apta y False si no lo es.
#Después, muestra el DataFrame completo con la nueva columna.

print ("Ejercicio 5")

condicion_1=(df["edad"] >= 22) & (df["puntos"] >= 40)
condicion_2=(df["edad"]<22) & (df["estudios_superiores"]) & (df["puntos"]>=35)

df["apto"] = condicion_1 | condicion_2

print(df)

# Ejercicio 6. Contar personas aptas y no aptas
# Usa pandas para contar cuántas personas son aptas y cuántas no.
# El objetivo es practicar el recuento de valores dentro de una columna.
#- Método recomendado: value_counts().

print( "Ejercicio 6")

conteo_aptos = df["apto"].value_counts()

print(conteo_aptos)

#Ejercicio 7. Filtrar candidatos aptos
#Crea un nuevo DataFrame llamado candidatos_aptos.
#Debe contener solo las personas que han sido aceptadas para el trabajo.
#Después, muestra esa tabla por pantalla.

print("Ejercicio 7")

candidatos_aptos = df[df["apto"]]
candidatos_no_aptos =df[~df["apto"]]

print(candidatos_aptos)
print(candidatos_no_aptos)

# Ejercicio 8: Filtrar candidatos con estudios superiores
#Crea otro DataFrame con las personas que tienen estudios superiores.
#Después, responde a las preguntas indicadas.


print("Ejercicio 8")
con_estudios_superiores=df[df["estudios_superiores"]]
contar_estudios_sup = len(con_estudios_superiores) # Cuántas personas tienen estudios superiores.
con_estudios_aptos =con_estudios_superiores["apto"].sum() #- Cuántas de ellas son aptas.
no_apto_con_estudio = con_estudios_superiores[~con_estudios_superiores["apto"]] #- Hay alguna persona con estudios superiores que no sea apta.
#no_apto_con_estudio =con_estudio_superiores[~con_estudios_superiores["apto"]].sum()

print(con_estudios_superiores)
print("Cantidad de personas con estudios sup:",contar_estudios_sup) 
print("Cantidad de personas aptas con estudios sup: ",con_estudios_aptos)

if len(no_apto_con_estudio) > 0:
    print("Personas no aptas con estudios superiores")
    print(no_apto_con_estudio[["nombre","edad","puntos"]])
else:
    print("No hay ninguno")

#Ejercicio 9. Ordenar los candidatos
#Ordena el DataFrame por la columna puntos.
#Debes mostrar la tabla ordenada de menor a mayor puntuación y después de mayor a menor
#puntuación.
#- Método recomendado: sort_values()
print("Ejercicio 9")

df_ascendente = df.sort_values(by="puntos") # 1. Ordenar de menor a mayor puntuación

df_descendente = df.sort_values (by="puntos",ascending=False)# 1. Ordenar de mayor a menor puntuación

print(df_ascendente)
print(df_descendente)

#Ejercicio 10. Calcular estadísticas
#Calcula estadísticas básicas usando pandas.
#Estas operaciones ayudan a interpretar los datos antes de tomar decisiones.
#- Edad media.
#- Puntuación media.
#- Puntuación máxima.
#- Puntuación mínima.
#- Edad de la persona más joven.
#- Edad de la persona más mayor.
#- Métodos útiles: mean(), max(), min().

print("Ejercicio 10")

edad_media =df ["edad"].mean()
puntaje_media =df ["puntos"].mean()
puntaje_maximo = df ["puntos"].max()
puntaje_minimo = df ["puntos"].min()
edad_min= df["edad"].min()
edad_max=df["edad"].max()

print("Edad media :", edad_media)
print("Puntaje medio :", puntaje_media)
print("Puntaje maximo :", puntaje_maximo)
print("Puntaje minimo :", puntaje_minimo)
print("Edad mayor de postulantes:", edad_max)
print("Edad menor de postulantes:", edad_min)