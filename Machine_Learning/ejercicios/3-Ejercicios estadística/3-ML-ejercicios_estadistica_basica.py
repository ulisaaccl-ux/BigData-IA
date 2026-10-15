import pandas as pd
df = pd.read_csv("Machine_Learning/ejercicios/3-Ejercicios estadística/datos_estadistica_alumnos.csv")
print(df)
#Ejercicio 1. Carga y exploración de datos
#- Carga el archivo CSV en un DataFrame llamado df.

df = pd.read_csv("Machine_Learning/ejercicios/3-Ejercicios estadística/datos_estadistica_alumnos.csv")
print(df)

#- Muestra las primeras filas.
print(df.head())

#- Guarda la columna puntos_prueba en una variable llamada puntos.

puntos = list(df["puntos_prueba"])

print(puntos)
#- Muestra cuántos datos hay en la columna.

contar_datos = len(df["puntos_prueba"])
print("Total de datos x columna :",contar_datos)

#- Explica con tus palabras qué representa cada fila del CSV.

#Respuesta: Cada fila se le conoce como caso, representa a un alumno individual con su identificador id recopilando sus atributos y variables.

#Ejercicio 2. Media
# Calcula la media de puntos_prueba con el Método 1: bucle for, acumulador y len().
# Calcula la misma media con el Método 2: sum(), len() y, si quieres practicarlo, map() con lambda.
# Calcula la misma media con el Método 3: pandas usando .mean().
# Muestra los tres resultados con nombres claros: media_bucle, media_funciones y media_pandas.
# Comprueba que los tres resultados coinciden.
# Explica qué significa esa media en el contexto de la prueba.

#Método 1: "Python elemental, usando listas, variables, for, condicionales, acumuladores e iteraciones."
suma = 0
for valor in puntos: 
    suma +=valor
media_bucle = suma / len (puntos)

print("Media (Bucle):", media_bucle)

#Método 2:  Python funcional, usando en cada caso la herramienta más adecuada: map(), filter(), lambda, sorted(), sum(), min(), max(), set() o count(). 
media_funciones = sum(map(lambda x: x, puntos)) / len(puntos)
print("Media (funciones): ",media_funciones)

#Método 3: pandas, usando métodos propios de Series y DataFrames.
media_panda = df["puntos_prueba"].mean()
print("Media (panda) :",media_panda)
print("La media significa que el promedio de los 10 alumnos en puntos es de 74 , también indica el valor central de los puntajes de todos los estudiantes")

#Ejercicio 3. Mediana
# Calcula la mediana de puntos_prueba con el Método 1: ordenar la lista, comprobar si la cantidad de datos es par o impar y acceder por índice.
# Calcula la misma mediana con el Método 2: sorted(), len() y acceso por índice. En este caso map() no es necesario.
# Calcula la misma mediana con el Método 3: pandas usando .median().
# Muestra los tres resultados con nombres claros: mediana_bucle, mediana_funciones y mediana_pandas.
# Comprueba que los tres resultados coinciden.
# Explica por qué la mediana representa el centro de los datos.

#Método 1: Python elemental (ordenar con bucles o sort básico, condicional par/impar)

puntos_ordenados_m1 = list(puntos)
# Ordenamos la lista (o usando .sort())
puntos_ordenados_m1.sort()

print("puntos ordenados: ",puntos_ordenados_m1)

#Contabilizamos la columna puntos_ordenados
n_m1 = len(puntos_ordenados_m1)


if n_m1 % 2 != 0:
    # Cantidad impar: elemento central exacto
    mediana_bucle = puntos_ordenados_m1[n_m1 // 2]
else:
    # Cantidad par: promedio de los dos elementos centrales
    pos1 = (n_m1 // 2) - 1
    pos2 = n_m1 // 2
    mediana_bucle = (puntos_ordenados_m1[pos1] + puntos_ordenados_m1[pos2]) / 2
print ("La mediana puntos (bucle) : ", mediana_bucle)

# Método 2: Python funcional (sorted, len y acceso por índice)

puntos_ordenados_m2 = sorted(puntos)
n_m2 = len(puntos_ordenados_m2)
if n_m2 % 2 != 0:
    mediana_funciones = puntos_ordenados_m2[n_m2 // 2]
else:
    mediana_funciones = (puntos_ordenados_m2[(n_m2 // 2) - 1] + puntos_ordenados_m2[n_m2 // 2]) / 2
print ("La mediana puntos (funciones): ", mediana_funciones)

# Método 3: Pandas

mediana_pandas = df["puntos_prueba"].median()
print("La mediana (pandas) :", mediana_pandas)

# Comprobación de que coinciden
print("¿Coinciden los tres métodos?:", mediana_bucle == mediana_funciones == mediana_pandas)

#Interpretacion del resultado:
# Representa el centro posicional de los datos porque divide la distribución en dos partes iguales: exactamente el 50% de los alumnos obtuvo una nota igual o menor a 75, y el otro 50% obtuvo una nota igual o mayor
