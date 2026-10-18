import pandas as pd
df = pd.read_csv("Machine_Learning/ejercicios/3-Ejercicios estadística/datos_estadistica_alumnos.csv")
print(df)
#Ejercicio 1. Carga y exploración de datos
print("Ejercicio 1 : Carga y exploración de datos")
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

print("Ejercicio 2 : Media")
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
print("Ejercicio 3 : Mediana")
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
print("Ejercicio 4 : Moda")
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
print("Ejercicio 5 : Desviación de cada dato respecto a la media")
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
print("Ejercicio 6 : Varianza")
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

#La varianza mide el grado de dispersión o separación de los datos respecto a su media aritmética, en este caso resulta 204.0

#Ejercicio 7. Desviación estándar
print("Ejercicio 7 : Desviación estándar")

# Calcula la desviación estándar con el Método 1: parte de la varianza calculada con bucles y aplica la raíz cuadrada.
# Calcula la misma desviación estándar con el Método 2: usa map(), lambda, sum(), len() y raíz cuadrada.
# Calcula la misma desviación estándar con el Método 3: pandas usando .std(ddof=0).
# Muestra los tres resultados con nombres claros: desviacion_estandar_bucle, desviacion_estandar_funciones y desviacion_estandar_pandas.
# Comprueba que los tres resultados coinciden o que solo cambian por pequeños decimales.
# Explica por qué la desviación estándar es más fácil de interpretar que la varianza.


# Método 1: Raíz cuadrada de la varianza del bucle (usando el operador ** 0.5)
desv_std_bucle = varianza_bucle ** 0.5
print("Varianza (bucle): ", desv_std_bucle)

# Método 2: Funciones (aplicando ** 0.5 a la varianza de funciones)
desv_std_funciones = varianza_funciones ** 0.5
print("varianza (funciones): ", desv_std_funciones)
# Método 3: Pandas (usando .std(ddof=0) para desviación poblacional)
desv_std_pandas = float(df["puntos_prueba"].std(ddof=0))
print("varianza (pandas): ", desv_std_pandas)

#Comprobación de que coinciden (redondeando a 4 decimales por precisión de coma flotante)
print("¿Coinciden los tres métodos?:", round(desv_std_bucle, 4) == round(desv_std_funciones, 4) == round(desv_std_pandas, 4))


#Interpretacion: Los alumnos se desvían o dispersan, en promedio, unos 14.28 puntos por encima o por debajo de la media (74.0 puntos).

# Ejercicio 8. Normalización min-max
print("Ejercicio 8 : Normalización min-max")
# Calcula el mínimo y el máximo de puntos_prueba.
# Normaliza cada valor con el Método 1: bucle for y append(), usando la fórmula (valor - mínimo) / (máximo - mínimo).
# Normaliza los mismos valores con el Método 2: min(), max(), map() y lambda.
# Normaliza los mismos valores con el Método 3: pandas usando .min(), .max() y operaciones sobre columnas. Crea una columna llamada puntos_normalizados.
# Muestra las tres versiones y comprueba que contienen los mismos valores.
# Explica qué significa que un valor normalizado sea 0, 0.5 o 1.

# 1. Obtener el mínimo y el máximo de puntos_prueba
min_val = min(puntos)  # 50
max_val = max(puntos)  # 100
rango = max_val - min_val  # 50

# Método 1: Bucle for y append()
puntos_norm_bucle = []
for p in puntos:
    norm = (p - min_val) / rango
    puntos_norm_bucle.append(round(norm, 4))

# Método 2: min(), max(), map() y lambda
puntos_norm_funciones = list(map(lambda p: round((p - min_val) / rango, 4), puntos))

# Método 3: Pandas (guardar en la columna puntos_normalizados)
df["puntos_normalizados"] = (df["puntos_prueba"] - df["puntos_prueba"].min()) / (df["puntos_prueba"].max() - df["puntos_prueba"].min())
puntos_norm_pandas = [round(float(x), 4) for x in df["puntos_normalizados"]]

print("Normalizados (Bucle):", puntos_norm_bucle)
print("Normalizados (Funciones):", puntos_norm_funciones)
print("Normalizados (Pandas):", puntos_norm_pandas)

#Interpretación :  0: Representa el valor mínimo de todo el conjunto de datos ; 0.5: Representa el punto medio exacto de la escala entre el mínimo y el máximo y 1: Representa el valor máximo del conjunto de datos

#Ejercicio 9. Estandarización z-score
print("Ejercicio 9 : Estandarización z-score")
# Calcula la media y la desviación estándar de puntos_prueba.
# Estandariza cada valor con el Método 1: bucle for y append(), usando la fórmula z = (valor - media) / desviación estándar.
# Estandariza los mismos valores con el Método 2: map(), lambda y las variables media y desviación estándar ya calculadas.
# Estandariza los mismos valores con el Método 3: pandas usando .mean(), .std(ddof=0) y operaciones sobre columnas. Crea una columna llamada puntos_estandarizados.
# Muestra las tres versiones y comprueba que contienen los mismos valores.
# Explica qué significa que un valor z sea positivo, negativo o cercano a 0.

# Variables base calculadas en pasos anteriores
media = float(media_panda)      # 74.0
desv_std = float(desv_std_pandas) # ~14.2829

# Método 1: Bucle for y append()
z_bucle = []
for p in puntos:
    z_val = (p - media) / desv_std
    z_bucle.append(round(z_val, 4))
print("z")
# Método 2: Funciones (map y lambda)
z_funciones = list(map(lambda p: round((p - media) / desv_std, 4), puntos))

# Método 3: Pandas (guardar en columna puntos_zscore)
# Usamos ddof=0 para mantener consistencia con la desviación estándar poblacional
df["puntos_zscore"] = (df["puntos_prueba"] - df["puntos_prueba"].mean()) / df["puntos_prueba"].std(ddof=0)
z_pandas = [round(float(x), 4) for x in df["puntos_zscore"]]

# Comprobación de coincidencia
print("¿Coinciden los tres métodos?:", z_bucle == z_funciones == z_pandas)

#Interpretación: 
# Z > 0 , indica que los puntos se situan por encima del promedio del grupo
# Z <0 ,  indica que los puntos se situan por debajo del promedio del grupo
# Z = 0, indica que los puntos de los alumnos son iguales al promedio

#Ejercicio 10. Interpretación final
print("Ejercicio 10 : Interpretación final ")
# Indica qué alumnos están por encima de la media usando el Método 1: bucle for y condicional.
# Indica los mismos alumnos usando el Método 2: filter() y lambda.
# Indica los mismos alumnos usando el Método 3: filtrado de pandas con condiciones sobre columnas.
# Indica qué alumnos están por debajo de la media usando también los tres métodos.
# Indica qué alumno o alumnos tienen el valor normalizado más alto.
# Indica qué alumno o alumnos tienen el valor normalizado más bajo.
# Indica si hay algún valor que parezca especialmente alejado del resto.
# Escribe una conclusión breve sobre el rendimiento general del grupo.

media = float(media_panda)  # 74.0

# 1. Alumnos por encima de la media (> 74)
# Método 1: Bucle for y condicional
encima_bucle = []
for i in range(len(df)):
    if df.loc[i, "puntos_prueba"] > media:
        encima_bucle.append(df.loc[i, "nombre"])

print("Alumnos encima de la media (bucle): ", encima_bucle)
# Método 2: filter() y lambda
encima_funciones = list(filter(lambda nombre: df.loc[df["nombre"] == nombre, "puntos_prueba"].values[0] > media, df["nombre"]))
print("Alumnos encima de la media (funciones): ", encima_funciones)
# Método 3: Filtrado de pandas
encima_pandas = list(df[df["puntos_prueba"] > media]["nombre"])
print("Alumnos encima de la media (pandas): ", encima_pandas)

# 2. Alumnos por debajo de la media (< 74)
# Método 1: Bucle for y condicional
debajo_bucle = []
for i in range(len(df)):
    if df.loc[i, "puntos_prueba"] < media:
        debajo_bucle.append(df.loc[i, "nombre"])
print("Alumnos por debajo de la media (bucle): ", debajo_bucle)

# Método 2: filter() y lambda
debajo_funciones = list(filter(lambda nombre: df.loc[df["nombre"] == nombre, "puntos_prueba"].values[0] < media, df["nombre"]))
print("Alumnos por debajo de la media (funciones): ", debajo_funciones)
# Método 3: Filtrado de pandas
debajo_pandas = list(df[df["puntos_prueba"] < media]["nombre"])
print("Alumnos por debajo de la media (pandas): ", debajo_pandas)

# 3. Alumno(s) con el valor normalizado más alto (máximo = 1.0)
max_norm = df["puntos_normalizados"].max()
alumnos_max_norm = list(df[df["puntos_normalizados"] == max_norm]["nombre"])
print("Alumno con el valor mas alto: ", alumnos_max_norm)
#Respuesta : Lucia tiene el puntaje mas alto con 100

# 4. Alumno(s) con el valor normalizado más bajo (mínimo = 0.0)
min_norm = df["puntos_normalizados"].min()
alumnos_min_norm = list(df[df["puntos_normalizados"] == min_norm]["nombre"])
print("Alumno con el valor mas bajo: ", alumnos_min_norm)
#Respuesta : Ana tiene el puntaje mas bajo  con 50

# RPTA: Caso de outlayer no existe, la progresion es bastante homogenea, la diferencia respecto a la media es de +/- 26 puntos, con z = 1.82.

# RPTA: El rendimiento del grupo es favorable y equilibrado, con una media de 74 una mediana de 75 y una moda de 80, se observa que el 50% de los estudiantes obtuvo una calificacion superior a 80, situandose por encima de la media.


