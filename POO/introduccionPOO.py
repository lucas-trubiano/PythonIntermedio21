# https://j2logo.com/python/tutorial/programacion-orientada-a-objetos/

# Pilares:
#  - Herencia (Simple/Multiple, isinstance()/issubclass())
#
#  - Abstraccion (Poder meter todo dentro de un modulo
#                 y usarlo sin saber como anda
#                 especificamente)
#
#  - Polimorfismo (cada objeto hace el mismo metodo
#                  de forma diferente)
#
#  - Encapsulamiento (Atributos privados)

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

# Metodos por defecto:
#  * __init__()
#  * __str__()
#  * __del__()

# Metodos estáticos:
#  * se crean con un @staticmethod

# ==================== Comencemos ====================
