#Define la clase Coche. Dentro de ella, escribe un __init__ que reciba la marca y el modelo y los guarde como atributos de cada objeto.
#Una vez definida la clase, fuera de ella:
# Crea dos objetos que representen coches distintos.
# Muestra la marca y el modelo de cada uno.
# Cambia el modelo del primer coche y comprueba que el segundo conserva el suyo.
print ( "______Ejercicio 1______")

# 1. Definición de la clase
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca      # Atributo marca
        self.modelo = modelo    # Atributo modelo

# 2. Creación de dos objetos distintos
coche1 = Coche("Seat", "Ibiza")
coche2 = Coche("Toyota", "Hybrid")

# 3. Mostrar la marca y modelo de cada uno
print(f"Coche 1: {coche1.marca} {coche1.modelo}")
print(f"Coche 2: {coche2.marca} {coche2.modelo}")

# 4. Cambiar el modelo del primer coche
coche1.modelo = "León"

# 5. Comprobar que el segundo coche conserva su modelo original
print("Comprobación tras la modificacion del coche")
print(f"Coche 1: {coche1.marca} {coche1.modelo}")
print(f"Coche 2: {coche2.marca} {coche2.modelo}")

#2. Modificar el estado de un objeto
#Escribe la definición completa de la clase CochePruebas. Los tres métodos siguientes deben quedar definidos dentro del cuerpo de la clase:
# __init__(): crea el atributo de instancia velocidad con valor inicial 0, en km/h.
# acelerar(): aumenta en 10 la velocidad del propio objeto.
# detener(): pone a cero la velocidad del propio objeto.
#Después de terminar la definición de la clase, fuera de ella, crea dos coches de pruebas. Llama a sus métodos para acelerarlos un número distinto de veces y detén solo uno. Comprueba que cada coche conserva su propia velocidad y que detener uno no cambia la del otro.
print ( "______Ejercicio 2______")
# Definición de la clase
class CochePruebas:
    def __init__(self):
        self.velocidad = 0 # Estado inicial: velocidad en 0 km/h
    def acelerar (self):
        self.velocidad += 10 # Aumenta en 10 la velocidad del propio objeto
    def detener (self):
        self.velocidad=0 #Detiene la velocidad a 0 del propio objeto
 # 2. Creación de dos coches de pruebas fuera de la clase
coche_a = CochePruebas()
coche_b = CochePruebas()

# Aceleramos coche_a 2 veces (debería llegar a 20 km/h)
coche_a.acelerar()
coche_a.acelerar()

# Aceleramos coche_b 3 veces (debería llegar a 30 km/h)
coche_b.acelerar()
coche_b.acelerar()
coche_b.acelerar()

print("Velocidades tras acelerar:")
print(f"Coche a: {coche_a.velocidad} km/h")
print(f"Coche b: {coche_b.velocidad} km/h")

coche_b.detener() # Detener solo uno de ellos

# 5. Comprobar que cada uno conserva su velocidad
print("Velocidades tras detener el coche b:")
print(f"Coche a: {coche_a.velocidad} km/h") 
print(f"Coche b: {coche_b.velocidad} km/h")  # Este es el que se quedaría en 0

#3. Heredar atributos y métodos
# Define una clase Vehiculo. Su inicializador debe guardar marca y modelo, y su método describir() debe devolver un texto que incluya ambos atributos.
# Define después una clase CocheElectrico que herede de Vehiculo. Dentro de ella, escribe un inicializador que reutilice el de Vehiculo mediante super() y guarde también autonomia_km.
# Utiliza describir() por herencia, sin volver a definirlo.
# Fuera de las clases, crea un coche eléctrico y comprueba que puedes consultar sus tres atributos y utilizar la descripción heredada.
print ( "______Ejercicio 3______")

class vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def describir(self):
        return f"Vehículo: {self.marca} Modelo: {self.modelo}" # Devolver un texto que incluya ambos atributos
    
# Definición de la subclase CocheElectrico
class CocheElectrico(vehiculo):
    def __init__(self,marca,modelo,autonomia_km):
        super().__init__(marca,modelo)
          # Reutilizamos el inicializador de Vehiculo con super()
        self.autonomia_km =autonomia_km

# Comprobaciones fuera de las clases:
coche_electrico = CocheElectrico("Audi","Audi Q5", 450)

# Printeamos los siguientes atributos:
print(f"Marca: {coche_electrico.marca}")
print(f"Modelo: {coche_electrico.modelo}")
print(f"Autonomía: {coche_electrico.autonomia_km} km")

# Utilizamos la descripcion heredada.
print(coche_electrico.describir())

#4. Sobrescribir un método heredado
# Define una clase Motor para representar motores de coches. Su inicializador debe guardar modelo y su método arrancar() debe devolver "Motor en marcha". Crea dos subclases:
#- MotorGasolina: su método arrancar() debe devolver "Motor de gasolina en marcha".
#- MotorElectrico: su método arrancar() debe devolver "Motor eléctrico en marcha".
# Ambas subclases deben utilizar el inicializador heredado de Motor, sin definir otro __init__.
# Después, crea un motor de cada tipo con modelos distintos y comprueba sus modelos y mensajes de arranque.
print ( "______Ejercicio 4______")

class Motor:
    def __init__(self,modelo):
        self.modelo = modelo
    def arrancar(self):
        return "Motor en marcha"
    
class MotorGasolina(Motor): # Subclase MotorGasolina (hereda el __init__ de Motor y sobrescribe arrancar)
    def arrancar(self):
        return "Motor de gasolina en marcha"
class MotorElectrico(Motor): # Subclase MotorElectrico (hereda el __init__ de Motor y sobrescribe arrancar)
    def arrancar(self):
        return "Motor eléctrico en marcha"

 # Creación de un motor de cada tipo fuera de las clases
gasolina = MotorGasolina("MotorGasX")
electrico = MotorElectrico("MotorElectricY")

# 5. Comprobación de modelos y mensajes de arranque
print(f"Modelo: {gasolina.modelo}")
print(f"Arranque: {gasolina.arrancar()}")      

print(f"Modelo: {electrico.modelo}")
print(f"Arranque: {electrico.arrancar()}")

#5. Utilizar el polimorfismo
# Reutiliza las clases del ejercicio anterior. Escribe una función poner_en_marcha(motor) que llame al método arrancar() del objeto recibido y devuelva su resultado. Después:
#- Crea una lista con un objeto MotorGasolina y otro MotorElectrico.
#- Recorre la lista con un bucle y utiliza poner_en_marcha() para mostrar el mensaje de cada motor.
# La función debe funcionar sin comprobar el tipo del motor con type() o isinstance().
# Finalmente, añade una clase MotorDiesel que herede de Motor y cuyo método arrancar() devuelva "Motor diésel en marcha". Incorpora un motor diésel a la lista y comprueba que funciona sin modificar la función poner_en_marcha() ni el bucle

print ( "______Ejercicio 5______")

# --- Clases base y derivadas (del Ejercicio 4) ---
def poner_en_marcha(motor):
    return motor.arrancar()

lista_motores = [MotorGasolina("PureTech"), MotorElectrico("Dual Motor")] # Lista solo con MotorGasolina y MotorElectrico

# Recorremos la lista y llamamos a la función
for m in lista_motores:
    print(poner_en_marcha(m))

class MotorDiesel(Motor):  # Añadimos la clase MotorDiesel
    def arrancar(self):
        return "Motor diésel en marcha"

lista_motores.append(MotorDiesel("2.0 TDI"))  #Incorporamos un motor diésel a la lista ya existente

print("\nLista con el motor diésel añadido:")  # Comprobamos que el bucle y la función funcionan sin modificarlos
for m in lista_motores:
    print(poner_en_marcha(m))

# 6. Ampliar un método heredado con super()
# Retoma las clases del ejercicio 3. Escribe una nueva versión de CocheElectrico que conserve su inicializador y defina su propio método describir().
# Ese método debe aprovechar la descripción de Vehiculo mediante super(), añadir una frase con la autonomía en kilómetros y devolver el mensaje completo. Reutiliza la descripción original sin volver a escribirla manualmente.
# Una vez definida esta versión de la clase, crea un coche eléctrico y comprueba tanto la descripción ampliada como la conservación de sus atributos.
print ( "______Ejercicio 6______")

# 1. Nueva versión de CocheElectrico
class CocheElectrico(vehiculo):
    def __init__(self, marca, modelo, autonomia_km):
        super().__init__(marca, modelo)
        self.autonomia_km = autonomia_km
    def describir(self):
        descripcion_base = super().describir()
        return f"{descripcion_base}. Autonomía: {self.autonomia_km} km."
    
electrico_ampliado = CocheElectrico("Hyundai", "Ioniq 5", 480)  #Creación del objeto

# 3. Comprobación de atributos
print(f"Marca: {electrico_ampliado.marca}")
print(f"Modelo: {electrico_ampliado.modelo}")
print(f"Autonomía: {electrico_ampliado.autonomia_km} km")

# 7. Mostrar datos con f-strings

# Escribe un único print() con una f-string que inserte los valores de las tres variables en una frase legible.
# Después, cambia los valores de las variables y comprueba que el mensaje se actualiza sin modificar el print(). No necesitas crear ninguna clase.
print ( "______Ejercicio 7______")
marca = "Seat"
modelo = "Ibiza"
anio = 2020
print(f"Vehículo registrado: {marca} {modelo}, matriculado en el año {anio}.")
marca = "Renault"
modelo = "Clio"
anio = 2023
print(f"Vehículo registrado: {marca} {modelo}, matriculado en el año {anio}.")

# 8. Gestionar una entrada incorrecta con try y except
# Pide al usuario los kilómetros recorridos por un coche con input() e intenta convertirlos a un entero con int() dentro de un bloque try.
# - Si la conversión funciona, muestra "Kilómetros indicados:" seguido del número.
# - Si se produce ValueError, muestra "Debes escribir un número entero.".
# - Fuera del try / except, muestra siempre "Programa finalizado.".
# Haz dos pruebas en ejecuciones distintas: introduce primero 12000 y después doce mil.
# Comprueba que el programa muestra el mensaje adecuado y llega al mensaje final en ambos casos
print ( "______Ejercicio 8______")
entrada = input("Introduce los kilómetros recorridos: ")
try: 
    km = int(entrada)
    print(f"Kilómetros indicados: {km}")
except ValueError:
    print("Debes escribir un número entero.")
# Instrucción fuera del bloque try / except (se ejecuta siempre)
print("Programa finalizado.")
# Hice la prueba con km : 12000 y otro con "DOCEMIL" y me printearon el try y except

