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

# Ejercicio 4. Moda
# Calcula la moda de puntos_prueba con el Método 1: recorre la lista con un bucle y crea un diccionario de frecuencias.
# Calcula la misma moda con el Método 2: usa set(), count(), max() y una lambda para encontrar el valor más repetido.
# Calcula la misma moda con el Método 3: pandas usando .mode().
# Muestra los tres resultados con nombres claros: moda_bucle, moda_funciones y moda_pandas.
# Comprueba que los tres resultados coinciden.
# Explica qué significa que ese valor sea la moda.

# Método 1: Bucle for y diccionario de frecuencias
frecuencias = {}
for valor in puntos:
    if valor in frecuencias:
        frecuencias[valor] += 1
    else:
        frecuencias[valor] = 1

# Encontrar la clave con la mayor frecuencia acumulada
moda_bucle = None
max_frecuencia = 0
for clave, cant in frecuencias.items():
    if cant > max_frecuencia:
        max_frecuencia = cant
        moda_bucle = clave
print("La Moda de puntos de prueba (bucle): ", moda_bucle)

# Método 2: Python funcional (set, count, max y key)
# set(puntos) toma los valores únicos y max() evalúa cuál se repite más mediante puntos.count
moda_funciones = max(set(puntos), key=lambda x: puntos.count(x))

print("La moda de puntos de prueba (funcional): ", moda_funciones)

# Método 3: pandas usando .mode().
moda_pandas = df["puntos_prueba"].mode()[0]
print("La moda de puntos de prueba (panda): ", moda_pandas)

# Comprobación de que coinciden
print("¿Coinciden los tres métodos?:", moda_bucle == moda_funciones == moda_pandas)

#Ejercicio 5. Desviación de cada dato respecto a la media
# Calcula primero la media de puntos_prueba.
# Calcula una lista de desviaciones con el Método 1: bucle for y append(). Cada valor debe ser punto - media.
# Calcula la misma lista con el Método 2: map() y lambda.
# Calcula las mismas desviaciones con el Método 3: pandas, restando la media directamente a la columna y creando una columna llamada desviacion.
# Muestra las tres versiones y comprueba que contienen los mismos valores.
# Explica qué significa que una desviación sea positiva, negativa o cero.

media = media_panda  # 74.0

# Método 1: Bucle for y append()
desviaciones_bucle = []
for p in puntos:
    desviaciones_bucle.append(p - media)
print("Desviacion (bucle): ", desviaciones_bucle)

# Método 2: map() y lambda
desviaciones_funciones = list(map(lambda p: p - media, puntos))
print("desviaciones (funciones): ", desviaciones_funciones)

# Método 3: Pandas (crear columna en el DataFrame)
df["desviacion"] = df["puntos_prueba"] - df["puntos_prueba"].mean()
desviaciones_pandas = list(df["desviacion"])
print("desviaciones (panda): ", desviaciones_pandas)

# Comprobación de que coinciden
print("¿Coinciden los tres métodos?:", desviaciones_bucle == desviaciones_funciones == desviaciones_pandas)

#Positiva (> 0): Indica que la nota del alumno está por encima de la media del grupo (por ejemplo, +6.0 o +26.0).
#Negativa (< 0): Indica que la nota del alumno está por debajo de la media del grupo (por ejemplo, -24.0 o -14.0).
#Cero (= 0): Significa que la nota del alumno coincide exactamente con la media general.

#Ejercicio 6. Varianza
# Calcula la varianza de puntos_prueba con el Método 1: bucle for, desviaciones, cuadrados y promedio final.
# Recuerda: primero se calcula cada desviación, después se eleva al cuadrado y finalmente se hace la media de esos cuadrados.
# Calcula la misma varianza con el Método 2: map(), lambda, sum() y len().
# Calcula la misma varianza con el Método 3: pandas usando ddof=0.
# Muestra los tres resultados con nombres claros: varianza_bucle, varianza_funciones y varianza_pandas.
# Comprueba que los tres resultados coinciden.
# Explica qué nos dice la varianza sobre el grupo.

# Usamos la media calculada previamente
media = float(media_panda)

# Método 1: Bucle for, acumulador de desviaciones al cuadrado y división por n
suma_cuadrados = 0
n=len(puntos)
for p in puntos:
    suma_cuadrados += (p - media) ** 2

varianza_bucle = suma_cuadrados / n

print("La varianza (bucle): ", varianza_bucle)

# Método 2: Funciones (sum, map y lambda dividiendo entre len)
varianza_funciones = sum(map(lambda p: (p - media) ** 2, puntos)) / n
print("La varianza (funciones): ",varianza_funciones)

# Método 3: Pandas (usando ddof=0 para varianza poblacional)
varianza_pandas = float(df["puntos_prueba"].var(ddof=0))
print("La varianza(pandas): ",varianza_pandas)

# Comprobación de que coinciden
print("¿Coinciden los tres métodos?:", varianza_bucle == varianza_funciones == varianza_pandas)

#Explicación del resultado.
#¿Qué representa la varianza y por qué sus unidades están al cuadrado?

La varianza mide el grado de dispersión o separación de los datos respecto a su media aritmética, en este caso resulta 204.0

