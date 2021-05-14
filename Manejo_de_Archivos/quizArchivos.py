# # 1) que direccion poner
# a="/IA2/TP1/orders.txt"
# b="/TP1/orders.txt"
# c="TP1/orders.txt"             #this
# d="IA2/TP1/orders.txt"
# e="orders.txt"
# X = c
# f = open(X)
# f.close()

# # 2) que pasa si no lo cierro
# import os

# path, _ = os.path.split(os.path.abspath(__file__))
# f = open(path+"/saludo.txt") # Abrimos el archivo correctamente

# print("El archivo es:\n================================")
# for linea in f:
#     print(linea,end="")
# print()
# # Output:

# # El archivo es:
# # ================================
# # Bienvenidos al manejo de archivos con python
# # Mi nombre es Lucas
# # Trabajo en Casa del futuro godoy cruz
# # Adios

# lineas = f.readlines() # en una lista cargo todas las lineas
# cantLineas = len(lineas)
# print(f"================================\nY tiene {cantLineas} lineas")
# # Output:

# # ================================
# # Y tiene 0 lineas

# 3) Que pasa si lo abro y quiero escribir
import os

path, _ = os.path.split(os.path.abspath(__file__))
f = open(path+"/saludo.txt","r") # Abrimos el archivo correctamente

"""### Archivo original:
Bienvenidos al manejo de archivos con python
Mi nombre es Lucas
Trabajo en Casa del futuro godoy cruz
Adios
"""

print("El archivo es:\n================================")
for linea in f:
    print(linea,end="")
print()

f.write("\nPongamos una linea al final")
print(f.readline())

f.close()