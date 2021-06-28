
class usuario():
    
    def __init__(self,nombre,contra):
        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 3
    
    def conectar(self):
        myPass = input("Ingrese su contraseña: ")
        if myPass==self.contra:
            print("Se ha conectado correctamente")
            self.conectado = True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                print("Contraseña incorrecta, intente de vuelta...")
                print("Intentos restantes: ",self.intentos)
                self.conectar()
            else:
                print("Error, no se pudo conectar")
                self.conectado = False
    
    def desconectar(self):
        if self.conectado:
            print("Se ha cerrado sesion")
            self.conectado = False
        else:
            print("Error")
    
    def __str__(self):
        if self.conectado:
            conect = "conectado"
        else:
            conect = "desconectado"
        return f"Mi nombre de usuario es: {self.nombre} y estoy {conect}"

# crear usuarios
user1 = usuario(input("Nombre: "),input("Contraseña: "))
print(user1)
user1.conectar()
print(user1)