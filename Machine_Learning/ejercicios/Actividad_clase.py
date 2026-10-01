
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

