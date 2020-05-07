

class Humano():  # Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion, estatura):  # Definimos el parametro edad , nombre y ocupacion
        self.edad = edad  # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre  # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion  # DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACION
        self.estatura = estatura
        # Creación de un nuevo método

    def presentar(self):
        presentacion = "Hola soy {}, mi edad es {} y mi ocupación es {} y mido {} mts"  # Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion, self.estatura))  # Usamos FORMAT


Persona1 = Humano(44, "Miguel", "Desocupado",1.82)  # Instancia

# Llamamos al método

Persona1.presentar()