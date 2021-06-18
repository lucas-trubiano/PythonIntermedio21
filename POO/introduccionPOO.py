# https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/

# Pilares:
#  - Abstraccion
#  - Encapsulamiento
#  - Herencia
#  - Polimorfismo

# Objeto:
#  - Atributos (datos, variables) (individuales o globales)
#  - Metodos (funciones)

class People():
    nacionalidad = "Argentina"

    def __init__(self,nombre,dni,nacionalidad=None):        # __init()__ -> Constructor
        self.nombre = nombre # input("Como te llamas? ")    # } -> Atributo
        self.dni = dni # input("Cual es tu dni? ")

    def caminar(self,pasos):                                # } -> Metodo
        print(f"Caminando {pasos} pasos")


class Usuario(): # Esta es la clase

    nacionalidad = "Argentina"
    cantUsuarios = 0

    def __init__(self,miNombre,miApellido,miEdad):
        self.nombre = miNombre
        self.apellido = miApellido
        self.edad = miEdad
        Usuario.cantUsuarios += 1
    
    def mePresento(self):
        print("Mi nombre es",self.nombre,self.apellido,f"y tengo {self.edad} años")

usuario1 = Usuario("Lucas","Trubiano",23) # Este es un objeto
usuario2 = Usuario("Python","POO",3) # Este es otro...

usuario1.mePresento() # Acceder a un atributo, desde afuera
usuario2.mePresento() # Acceder a un atributo, desde afuera

print(Usuario.cantUsuarios)

# Metodos por defecto:
#  * __init__()
#  * __str__()
#  * __del__()

# Metodos estáticos:
#  * se crean con un @staticmethod

# ==================== Comencemos ====================
#  - Abstraccion

#  - Encapsulamiento (Atributos privados)

#  - Herencia (Simple/Multiple, isinstance()/issubclass())

#  - Polimorfismo (cada objeto hace el mismo método
#                  de forma diferente)
